#Difficult
def flatten(arr):
    resultArr = []
    for element in arr:
        if type(element) is int:
            resultArr.append(element)
        else:
            resultArr.extend(flatten(element))
    return resultArr

print(flatten([1, 2, 3, [4,[5,6]]]))