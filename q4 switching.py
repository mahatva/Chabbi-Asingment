def ans(dictionary):
    return {v: k for k, v in dictionary.items()}

input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

fans = ans(input_dict)
print(fans)