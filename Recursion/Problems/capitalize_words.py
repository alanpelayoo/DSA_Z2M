def capitalizeWords(arr):
    capitalized_list = []

    if len(arr) == 0:
        return capitalized_list

    capitalized_list.append(arr[0].upper())
    return capitalized_list + capitalizeWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words) )