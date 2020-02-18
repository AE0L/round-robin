from functions import cat
from functions import mul
from functions import prop
from functions import strlen
from functions import reduce
from functions import foreach
from functions import if_else
from functions import getter as get
from functions import surround as surr

# Box Characters
HSL = u'\u2500' # ─
UDR = u'\u251C' # ├
UDL = u'\u2524' # ┤
CRS = u'\u253C' # ┼

class Gantt:
    def __init__(self, data, margin=0):
        self.data   = data
        self.margin = margin

    def print(self):
        times  = list(map(lambda a: str(prop(a, 'Time')), self.data))
        queues = list(map(get('Queue'), self.data))

        # Time Stamps
        time_stamps = mul(' ', self.margin)

        for i in range(len(times) - 1):
            if len(times[i]) == 2:
                time_stamps += cat(times[i], mul(' ', strlen(queues[i][0]) + 1))
            elif len(times[i]) == 3:
                time_stamps += cat(cat('\b', times[i]), mul(' ', strlen(queues[i][0]) + 1))
            elif len(times[i]) == 4:
                time_stamps += cat(cat('\b', times[i]), mul(' ', strlen(queues[i][0])))
            else:
                time_stamps += cat(times[i], mul(' ', strlen(queues[i][0]) + 2))

        time_stamps += if_else(len(times[-1]) >= 3, cat('\b', times[-1]), times[-1])

        print(time_stamps)

        # Line Drawing
        lines = mul(' ', self.margin)

        for i in range(len(times)):
            if i == 0:
                lines += UDR
            elif i == len(times) - 1:
                lines += mul(HSL, strlen(queues[i - 1][0]) + 2) + UDL
            else:
                lines += mul(HSL, strlen(queues[i - 1][0]) + 2) + CRS

        print(lines) # Lines

        # PIDs
        cat_s = lambda a, b: cat(b, cat(surr(queues[a][0], ' '), ' '))
        pids  = cat(' ', mul(' ', self.margin))
        pids  = (reduce(cat_s, range(len(queues) - 1), pids))

        print(pids) # PIDs
