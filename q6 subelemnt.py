def ans(li, si, ei):
    sublist = li[si:ei:2]
    return sublist

li = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
si = 2
ei = 9

fans = ans(li, si, ei)
print(fans)
