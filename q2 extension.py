def ans(combo, filenames):

    ap = {}
    pairs = combo.split(';')

    for x in pairs:
        extension, file_type = x.split(',')
        ap[extension] = file_type

    result = {}
    for x in filenames:
        extension = x.split('.')[-1]
        file_type = ap.get(extension, 'unknown')
        result[x] = file_type

    return result


combo = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

fans = ans(combo, filenames)
print(fans)
