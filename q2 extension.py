def get_file_types(extension_type_string, filenames):

    extension_type_pairs = {}
    pairs = extension_type_string.split(';')

    # Create a dictionary with extension:type pairs
    for pair in pairs:
        extension, file_type = pair.split(',')
        extension_type_pairs[extension] = file_type

    result = {}

    # Iterate through the filenames and determine their types
    for filename in filenames:
        # Extract the extension from the filename
        extension = filename.split('.')[-1]

        # Determine the type based on the extension
        file_type = extension_type_pairs.get(extension, 'unknown')

        # Add the filename:type pair to the result dictionary
        result[filename] = file_type

    return result


types = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = get_file_types(types, filenames)
print(result)
