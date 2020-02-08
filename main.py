from round_robin import round_robin
from functions import foreach

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

result = round_robin(sched_data_2, 3)

foreach(lambda x: print('TIME:', x['time'], ', QUEUE:', x['queue']), result['gantt'])
print('\ntotal time              :', result['total_time'])
print('Average Turn-Around Time:', result['avg_tt'])
print('Average Waiting Time    :', result['avg_wt'])
print('\nScheduling Result:')
foreach(print, result['sched'])
