from job_queue import JobQueue
from functions import prop
from functions import every

is_complete    = lambda j: j['rem'] == 0
sched_complete = lambda s: every(lambda j: is_complete(j), s)
gantt_chart    = lambda q, g: lambda t: g.append({'time': t, 'queue': list(map(lambda a: a['job'], q.to_array()))})
prepare_data   = lambda d: list(map(lambda j: prop(j, 'rem', j['BT']), d))

# Round Robin Algorithm
# Q           - Quantum Time
# sched       - Process schedule
# time        - Current time
# queue       - Process queue
# gantt       - Gantt chart
# expiration  - Quantum interval
# record_time - Gantt Chart updater
def round_robin(data, Q):
    sched       = prepare_data(data[:])
    time        = 0
    queue       = JobQueue()
    gantt       = []
    expiration  = time + Q
    record_time = gantt_chart(queue, gantt)

    while not sched_complete(sched):
        for job in sched:
            if job['AT'] == time:
                queue.enqueue(job)
                record_time(time)

        if time < expiration:
            if queue.peek()['rem'] == 0:
                queue.dequeue()
                expiration = time + Q
                record_time(time)
            
            queue.decrease_rem_time()
        elif time == expiration:
            process = queue.dequeue()

            if not process['rem'] == 0:
                queue.enqueue(process)
                
            queue.decrease_rem_time()
            expiration += Q
            record_time(time)

        time += 1

    queue.dequeue()
    record_time(time)

    for x in gantt:
        print('time:', x['time'], ', queue:', x['queue'])
    print('\ntotal time:', time)


# Sample Data from https://en.wikipedia.org/wiki/Round-robin_scheduling
# job - Process Name/ID
# AT  - Arrival Time
# BT  - Burst Time
sched_data = [
    {'job': 0, 'AT': 0, 'BT': 250},
    {'job': 1, 'AT': 50, 'BT': 170},
    {'job': 2, 'AT': 130, 'BT': 75},
    {'job': 3, 'AT': 190, 'BT': 100},
    {'job': 4, 'AT': 210, 'BT': 130},
    {'job': 5, 'AT': 350, 'BT': 50}
]

# Run algorithm
round_robin(sched_data, 100)
