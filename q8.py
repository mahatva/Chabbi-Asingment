# ANS
# A0 : {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# A1 : range(0, 10)
# A2 : []
# A3 : [1, 2, 3, 4, 5]
# A4 : [1, 2, 3, 4, 5]
# A5 : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# A6 : [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# A7 : 21
# A8 : <map object at 0x100a27d60>
# A9 : <filter object at 0x100a27cd0>


from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, ['I' , 'want', 'to', 'learn', 'python'])


variables = []

variables.append(A0)
variables.append(A1)
variables.append(A2)
variables.append(A3)
variables.append(A4)
variables.append(A5)
variables.append(A6)
variables.append(A7)
variables.append(A8)
variables.append(A9)

for x, var in enumerate(variables):
    print("A"+ str(x) ,":" , var)


