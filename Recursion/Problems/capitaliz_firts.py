
# def capitalizeFirst(arr):
#     for i in range(len(arr)):
#         element = arr[i]
#         arr[i] = element[0].upper() + element[1:]
#     return arr

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:]) 

print(capitalizeFirst(['car', 'taco', 'banana']))