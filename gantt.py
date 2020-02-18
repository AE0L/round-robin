from functions import getter as get, strlen, reduce, cat, mul
from functions import arr_to_string as to_str

HSL = u'\u2500' # ─
UDR = u'\u251C' # ├
UDL = u'\u2524' # ┤
CRS = u'\u253C' # ┼

class Gantt:
    def __init__(self, data, quantum, margin=0):
        self.data   = data
        self.margin = margin

    def print(self):
        times  = to_str(map(get('Time'), self.data))
        queues = list(map(get('Queue'), self.data))

        s = mul(' ', self.margin)

        for i in range(len(times) - 1):
            if len(times[i]) == 2:
                s += cat(times[i], mul(' ', strlen(queues[i][0]) + 1))
            elif len(times[i]) == 3:
                s += cat(cat('\b', times[i]), mul(' ', strlen(queues[i][0]) + 1))
            elif len(times[i]) == 4:
                s += cat(cat('\b', times[i]), mul(' ', strlen(queues[i][0])))
            else:
                s += cat(times[i], mul(' ', strlen(queues[i][0]) + 2))

        if len(times[-1]) >= 3:
            s += '\b' + times[-1]
        else:
            s += times[-1]

        print(s) # Time Stamps

        s = ' ' * self.margin

        for i in range(len(times)):
            if i == 0:
                s += UDR
            elif i == len(times) - 1:
                s += mul(HSL, strlen(queues[i - 1][0]) + 2) + UDL
            else:
                s += mul(HSL, strlen(queues[i - 1][0]) + 2) + CRS

        print(s) # Lines

        s = cat(' ', mul(' ', self.margin))

        for i in range(len(queues) - 1):
            s += f' {queues[i][0]}  '

        print(s) # PIDs
