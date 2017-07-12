def add(arr1, arr2):
    new_arr = []
    for i in range(0, len(arr1)):
        if (type(arr1[0]) is list):
            new_arr.append([])
            for j in range(0, len(arr1[0])):
                new_arr[i].append(arr1[i][j] + arr2[i][j])
        else:
            new_arr.append(arr1[i] + arr2[i])
    return new_arr
