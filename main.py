class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, val):
        self.array.append(val)

    def dequeue(self):
        return self.array.pop(0)

    def value(self):
        return self.array


def sched_complete(sched):
    for job in sched:
        if job['rem'] > 0:
            return False
    return True


def update_gantt(queue, gantt):
    return lambda time: gantt.append({'time': time, 'queue': list(map(lambda a: a['job'], queue.value()))})


def round_robin(sched, quantum):
    time = 0
    queue = Queue()
    gantt = []
    quantum_interval = time + quantum
    record_time = update_gantt(queue, gantt)

    # Add "remaining" attribute to each job
    for job in sched:
        job['rem'] = job['BT']

    # Round Robin Algorithm
    while not sched_complete(sched):
        # Add the job/s that arrived in queue
        for job in sched:
            if job['AT'] == time:
                queue.enqueue(job)
                record_time(time)

        # If current process time is not yet expired
        if time < quantum_interval:
            # If current process finished before the expiration time
            if queue.value()[0]['rem'] == 0:
                tmp = queue.dequeue()
                quantum_interval = time + quantum
                record_time(time)
            
            queue.value()[0]['rem'] -= 1
            
        # If current process reached the expiration time
        elif time == quantum_interval:
            process = queue.dequeue()

            # Enqueue process if not finished
            if not process['rem'] == 0:
                queue.enqueue(process)
                
            queue.value()[0]['rem'] -= 1
            quantum_interval += quantum
            record_time(time)

        time += 1

    queue.dequeue()
    record_time(time)

    # Ouput Gantt Chart
    for x in gantt:
        print('time:', x['time'], ', queue:', x['queue'])
    print('\ntotal time:', time)


# Sample Data from https://en.wikipedia.org/wiki/Round-robin_scheduling
sched_data = [
    {'job': 0, 'AT': 0, 'BT': 250},
    {'job': 1, 'AT': 50, 'BT': 170},
    {'job': 2, 'AT': 130, 'BT': 75},
    {'job': 3, 'AT': 190, 'BT': 100},
    {'job': 4, 'AT': 210, 'BT': 130},
    {'job': 5, 'AT': 350, 'BT': 50}
]

# Run algorithm with sample data
round_robin(sched_data, 100)

    
