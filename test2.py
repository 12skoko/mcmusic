
import operator


a=[

{'note': 76, 'velocity': 71, 'chet': 9, 'time': 1},
{'note': 45, 'velocity': 71, 'chet': 6, 'time': 4},
{'note': 71, 'velocity': 71, 'chet': 10, 'time': 0},
{'note': 78, 'velocity': 71, 'chet': 8, 'time': 2},
{'note': 83, 'velocity': 71, 'chet': 6, 'time': 4},
{'note': 52, 'velocity': 74, 'chet': 6, 'time': 10}
    ]

sorted_x = sorted(a, key=operator.itemgetter('time'))
# sorted_x = sorted(a, key=lambda x : x['time'])


for i in sorted_x:
    print(i)