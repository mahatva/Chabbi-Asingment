def sortf(lst):
    for i in range(len(lst)):
        l = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[l]:
                l = j
        lst[i], lst[l] = lst[l], lst[i]
    return lst


given =  [5,416,54,21,6135,15,741]
fans = sortf(given)
print(fans)