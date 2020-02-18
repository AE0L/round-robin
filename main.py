from round_robin import round_robin
from table import Table
from functions import foreach, prop, getter_setter as get_set, replace
from gantt import Gantt

sched_data_1 = [
    {'PID': 'P1', 'AT': 0, 'BT': 250},
    {'PID': 'P2', 'AT': 50, 'BT': 170},
    {'PID': 'P3', 'AT': 130, 'BT': 75},
    {'PID': 'P4', 'AT': 190, 'BT': 100},
    {'PID': 'P5', 'AT': 210, 'BT': 130},
    {'PID': 'P6', 'AT': 350, 'BT': 50}
]

sched_data_2 = [
    {'PID': 'P1', 'AT': 0, 'BT': 10},
    {'PID': 'P2', 'AT': 1, 'BT': 4},
    {'PID': 'P3', 'AT': 2, 'BT': 5},
    {'PID': 'P4', 'AT': 3, 'BT': 3},
]

result  = round_robin(sched_data_1, 100)

get_res = lambda a: prop(result, a)
sched   = get_res('sched')
res_dtl = [get_res('result')]

sched_table  = Table(sched, title=f'Schedule Q={3}', margin=1)
gantt_chart  = Gantt(result['gantt'], margin=1)
result_table = Table(res_dtl, title='Result', margin=1)

sched_table.print()
print()
gantt_chart.print()
print()
result_table.print()

