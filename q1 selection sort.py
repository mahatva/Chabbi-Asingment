def selection_sort(lst):
    # Iterate through the entire list
    for i in range(len(lst)):
        # Find the index of the minimum element in the remaining unsorted part
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j

        # Swap the minimum element with the current element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst


my_list =  [5,416,54,21,6135,15,741]
sorted_list = selection_sort(my_list)
print(sorted_list)