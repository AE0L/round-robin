from job_queue import JobQueue
from functions import prop
from functions import every
from functions import reduce
from functions import foreach

is_complete     = lambda j: j['RM'] == 0
sched_complete  = lambda s: every(lambda j: is_complete(j), s)
prepare_data    = lambda d: list(map(lambda j: prop(j, 'RM', j['BT']), d))
gantt_chart     = lambda q, g: lambda t: g.append({
    'time': t, 'queue': list(map(lambda a: a['PID'], q.to_array()))
})
turnaround_time = lambda j: (j['complete'] - j['AT'])
waiting_time    = lambda j: (j['TT'] - j['BT'])
get_tt          = lambda j: prop(j, 'TT', turnaround_time(j))
get_wt          = lambda j: prop(j, 'WT', waiting_time(j))


def round_robin(data, Q):
    sched       = prepare_data(data[:])
    time        = 0
    queue       = JobQueue()
    gantt       = []
    q_time      = time + Q
    record_time = gantt_chart(queue, gantt)

    while not sched_complete(sched):
        for job in sched:
            if job['AT'] == time:
                queue.enqueue(job)
                record_time(time)

        if time < q_time:
            if queue.peek()['RM'] == 0:
                job             = queue.dequeue()
                job['complete'] = time
                q_time          = time + Q

                record_time(time)

            queue.decrease_rem_time()
        elif time == q_time:
            job = queue.dequeue()

            if not job['RM'] == 0:
                queue.enqueue(job)
            else:
                job['complete'] = time

            queue.decrease_rem_time()
            q_time += Q

            record_time(time)

        time += 1

    queue.dequeue()['complete'] = time

    record_time(time)

    foreach(get_tt, sched)
    foreach(get_wt, sched)

    avg_tt = round(reduce(lambda j, a: j['TT'] + a, sched, 0) / len(sched), 2)
    avg_wt = round(reduce(lambda j, a: j['WT'] + a, sched, 0) / len(sched), 2)

    for x in gantt:
        print('TIME:', x['time'], ', QUEUE:', x['queue'])

    print()
    print('total time              :', time)
    print('Average Turn-Around Time:', avg_tt)
    print('Average Waiting Time    :', avg_wt)
    print()
    print('Scheduling Result:')
    foreach(print, sched)


sched_data_1 = [
    {'PID': 0, 'AT': 0, 'BT': 250},
    {'PID': 1, 'AT': 50, 'BT': 170},
    {'PID': 2, 'AT': 130, 'BT': 75},
    {'PID': 3, 'AT': 190, 'BT': 100},
    {'PID': 4, 'AT': 210, 'BT': 130},
    {'PID': 5, 'AT': 350, 'BT': 50}
]

sched_data_2 = [
    {'PID': 'P1', 'AT': 0, 'BT': 10},
    {'PID': 'P2', 'AT': 1, 'BT': 4},
    {'PID': 'P3', 'AT': 2, 'BT': 5},
    {'PID': 'P4', 'AT': 3, 'BT': 3},
]

round_robin(sched_data_2, 3)
