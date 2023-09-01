

def sum_digits(numbr):
    assert numbr>= 0 and int(numbr) == numbr, 'numbr has to + integer only' 
    quotient = numbr//10
    remainder = numbr%10
    if numbr == 0:
        return 0
    
    return remainder + sum_digits(quotient)

print(sum_digits(5555))

