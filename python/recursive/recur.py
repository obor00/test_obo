def recursive_list(list_data):
    if not list_data:
        return []
    else:
        return [list_data[0]] + recursive_list(list_data[1:])

print(recursive_list([1,2,3,4])) # [1,2,3,4]
