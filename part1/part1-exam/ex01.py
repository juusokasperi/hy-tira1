def create_list(n):
    result = []
    to_add = 1
    for i in range(n):
        result.append(to_add)
        if to_add == 1:
            to_add = 2
        else:
            to_add = 1
    return result

