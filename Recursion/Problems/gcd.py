
def gcd(x,y):
    assert int(x) == x and int(y) == y, 'Must be integer'
    if x < 0:
        x = x*-1
    if y < 0:
        y = y*-1
    if y == 0:
        return x
    remainder = x%y
    return gcd(y,remainder)

print(gcd(48,18))



