def ans(imp, key):
    return sorted(imp, key=lambda x: x[key])

imp = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list = ans(imp, "fruit")
print(sorted_list)

sorted_list = ans(imp, "color")
print(sorted_list)
