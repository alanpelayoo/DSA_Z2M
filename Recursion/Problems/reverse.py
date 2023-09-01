def reverse(strng):
    if len(strng) == 1:
        return strng
    return reverse(strng[1:]) +strng[0] 

print(reverse("appmillers"))