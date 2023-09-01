

def isPalindrome(strng):
    if strng == "":
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])


print(isPalindrome('') )
