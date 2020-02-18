from job_queue import JobQueue
from functions import every, reduce, foreach, is_zero, append, getter 
from functions import getter_setter as accessor, if_then

# PID - Process ID
# AT  - Arrival Time
# BT  - Burst Time
# RM  - Remaining Time
# CMP - Completion Time
# TT  - Turn around Time
# WT  - Waiting Time
PID            = getter('PID')
AT             = getter('AT')
BT             = getter('BT')
RM             = accessor('RM')
CMP            = accessor('CMP')
TT             = accessor('TT')
WT             = accessor('WT')

calc_tt        = lambda j: CMP(j) - AT(j)
calc_wt        = lambda j: TT(j) - BT(j)
set_tt         = lambda j: TT(j, calc_tt(j))
set_wt         = lambda j: WT(j, calc_wt(j))
is_complete    = lambda j: is_zero(RM(j))
sched_complete = lambda s: every(is_complete, s)
prepare_data   = lambda d: list(map(lambda j: RM(j, BT(j)), d))
get_q_pids     = lambda q: list(map(PID, q.to_array()))
gantt_chart    = lambda q, g: lambda t: append(g, {
    'Time': t,
    'Queue': get_q_pids(q)
})


def round_robin(data, Q):
    sched       = prepare_data(data[:])
    time        = 0
    queue       = JobQueue()
    gantt       = []
    q_time      = time + Q
    record_time = gantt_chart(queue, gantt)

    # Start Algorithm
    while not sched_complete(sched):
        for job in sched:
            if AT(job) == time:
                queue.enqueue(job)

                if is_zero(time):
                    record_time(time)

        if time < q_time:
            if is_complete(queue.peek()):
                job    = queue.dequeue()
                q_time = time + Q
                CMP(job, time)
                record_time(time)

            queue.decrease_rem_time()
        elif time == q_time:
            job     = queue.dequeue()
            q_time += Q

            queue.enqueue(job) if not is_complete(job) else CMP(job, time)
            queue.decrease_rem_time()
            record_time(time)

        time += 1

    CMP(queue.dequeue(), time)
    record_time(time)
    # End Algorithm

    foreach(set_tt, sched)
    foreach(set_wt, sched)

    total_tt = reduce(lambda j, a: TT(j) + a, sched)
    total_wt = reduce(lambda j, a: WT(j) + a, sched)
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
