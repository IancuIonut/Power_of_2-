def power_of_two(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    result = []
    for num in arr:
        if num <= 0:
            result.append(0)
        elif num & (num - 1) == 0:
            result.append(1)
        else:
            result.append(0)
    return result

arr = [2, 4, 8, 10, 16, 20, 32]
result = power_of_two(arr)
print(result)


def power_of_two():
    """
    :rtype: List[int]
    """
    arr = input("Enter an array of integers, separated by commas: ").split(",")
    arr = [int(x.strip()) for x in arr]
    result = []
    for num in arr:
        if num <= 0:
            result.append(0)
        elif num & (num - 1) == 0:
            result.append(1)
        else:
            result.append(0)
    return result


result = power_of_two()
print(result)