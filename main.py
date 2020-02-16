from round_robin import round_robin
from table import Table
from functions import foreach, prop, getter_setter as get_set, replace

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

result  = round_robin(sched_data_2, 3)
get_res = lambda a: prop(result, a)
sched   = get_res('sched')
gantt   = get_res('gantt')
res_dtl = [get_res('result')]
queue   = get_set('Queue')
rem_quo = lambda a: queue(a, replace(queue(a), "'", ''))

foreach(rem_quo, gantt)

sched_table  = Table(sched, title='Schedule', margin=1)
gantt_table  = Table(gantt, title='Gantt Chart', margin=1)
result_table = Table(res_dtl, title='Result', margin=1)

sched_table.print()
print()
gantt_table.print()
print()
result_table.print()
