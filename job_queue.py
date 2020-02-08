class JobQueue:
    def __init__(self):
        self.array = []

    def enqueue(self, val):
        self.array.append(val)

    def dequeue(self):
        return self.array.pop(0)

    def decrease_rem_time(self):
        self.array[0]['rem'] -= 1

    def peek(self):
        return self.array[0]

    def to_array(self):
        return self.array
