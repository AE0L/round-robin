sched_data = [
        {'job': 0, 'AT': 0, 'BT': 250},
        {'job': 1, 'AT': 50, 'BT': 170},
        {'job': 2, 'AT': 130, 'BT': 75},
        {'job': 3, 'AT': 190, 'BT': 100},
        {'job': 4, 'AT': 210, 'BT': 130},
        {'job': 5, 'AT': 350, 'BT': 50}
    ]


class Queue:
    def __init__(self, init=[]):
        self.array = init

    def enqueue(self, item):
        self.array.append(item)

    def dequeue(self):
        return self.array.pop(0)

    def value(self):
        return self.array


def setup_sched(sched):
    for job in sched:
        job['rem'] = job['BT']
        
    return sched


def sched_is_complete(sched):
    for job in sched:
        if job['rem'] > 0:
            return False
    
    return True


def round_robin(sched, quantum):
    time = 0
    queue = Queue()
    gantt = []
    quantum_interval = time + quantum
    sched = setup_sched(sched)

    while not sched_is_complete(sched):
        for job in sched:
            if job['AT'] == time:
                queue.enqueue(job)
                gantt.append({'time': time, 'queue': list(map(lambda a: a['job'], queue.value()))})
                break

        if time < quantum_interval:            
            if queue.value()[0]['rem'] == 0:
                tmp = queue.dequeue()
                gantt.append({'time': time, 'queue': list(map(lambda a: a['job'], queue.value()))})
                quantum_interval = time + quantum
            
            queue.value()[0]['rem'] -= 1
        elif time == quantum_interval:
            tmp = queue.dequeue()

            if not tmp['rem'] == 0:
                queue.enqueue(tmp)
                
            queue.value()[0]['rem'] -= 1
            gantt.append({'time': time, 'queue': list(map(lambda a: a['job'], queue.value()))})

        if time == quantum_interval:
            quantum_interval += quantum

        time += 1

    queue.dequeue()

    gantt.append({'time': time, 'queue': queue.value()})

    for x in gantt:
        print('time:', x['time'], ', queue:', x['queue'])

    print('total time:', time)

round_robin(sched_data, 100)

    
