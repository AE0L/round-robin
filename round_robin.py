from job_queue import JobQueue
from functions import prop
from functions import set_prop
from functions import every
from functions import reduce
from functions import foreach
from functions import is_zero

# PID - Process ID
# AT  - Arrival Time
# BT  - Burst Time
# RM  - Remaining Time
# CMP - Completion Time
# TT  - Turn around Time
# WT  - Waiting Time
PID            = lambda j: prop(j, 'PID')
AT             = lambda j: prop(j, 'AT')
BT             = lambda j: prop(j, 'BT')
RM             = lambda j, v=None: prop(j, 'RM') if not v else set_prop(j, 'RM', v)
CMP            = lambda j, v=None: prop(j, 'CMP') if not v else set_prop(j, 'CMP', v)
TT             = lambda j, v=None: prop(j, 'TT') if not v else set_prop(j, 'TT', v)
WT             = lambda j, v=None: prop(j, 'WT') if not v else set_prop(j, 'WT', v)

calc_tt        = lambda j: CMP(j) - AT(j)
calc_wt        = lambda j: TT(j) - BT(j)
set_tt         = lambda j: TT(j, calc_tt(j))
set_wt         = lambda j: WT(j, calc_wt(j))

is_complete    = lambda j: is_zero(RM(j))
sched_complete = lambda s: every(lambda j: is_complete(j), s)
prepare_data   = lambda d: list(map(lambda j: RM(j, BT(j)), d))
gantt_chart    = lambda q, g: lambda t: g.append({
    'Time': t,
    'Queue': list(map(lambda a: PID(a), q.to_array()))
})


def round_robin(data, Q):
    sched       = prepare_data(data[:])
    time        = 0
    queue       = JobQueue()
    gantt       = []
    q_time      = time + Q
    record_time = gantt_chart(queue, gantt)

    while not sched_complete(sched):
        for job in sched:
            if AT(job) == time:
                queue.enqueue(job)
                record_time(time)

        if time < q_time:
            if is_complete(queue.peek()):
                job    = queue.dequeue()
                q_time = time + Q
                CMP(job, time)
                record_time(time)

            queue.decrease_rem_time()
        elif time == q_time:
            job = queue.dequeue()

            if not is_complete(job):
                queue.enqueue(job)
            else:
                CMP(job, time)

            queue.decrease_rem_time()
            q_time += Q
            record_time(time)

        time += 1

    CMP(queue.dequeue(), time)
    record_time(time)

    foreach(set_tt, sched)
    foreach(set_wt, sched)

    total_tt = reduce(lambda j, a: TT(j) + a, sched, 0)
    total_wt = reduce(lambda j, a: WT(j) + a, sched, 0)
    avg_tt   = round(total_tt / len(sched), 2)
    avg_wt   = round(total_wt / len(sched), 2)

    foreach(lambda a: a.pop('RM'), sched)

    return {
        'gantt': gantt,
        'result': {
            'Total Time': time,
            'Average TT': avg_tt,
            'Average WT': avg_wt
        },
        'sched': sched
    }
