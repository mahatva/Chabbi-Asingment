def switch_key_value_pairs(dictionary):

    return {v: k for k, v in dictionary.items()}

input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result_dict = switch_key_value_pairs(input_dict)
print(result_dict)