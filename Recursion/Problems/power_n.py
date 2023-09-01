
def power_n(x,n):
    assert int(n) == n and n>=0, 'the exponent has to be integer'
    if n == 0:
        return 1
    elif n <0:
        return 1/x * power_n(x,n+1)
        
    return x * power_n(x,n-1)

print(power_n(2,3))