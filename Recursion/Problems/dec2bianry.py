def decbinary(num):
    quotient = int(num/2)
    remainder = num %2
    if quotient == 0:
        return str(remainder)
    return  decbinary(quotient) + str(remainder)
#Solution 2  f(n) = n mod 2 + 10*f(n/2)
def decimalToBinary(n):
    assert int(n) == n, 'must be integer'
    if n == 0:
        return 0  
    return n%2 + decimalToBinary(int(n/2))*10
print(decbinary(10))
print(decimalToBinary(10))