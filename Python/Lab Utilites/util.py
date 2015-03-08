#
# getInt
#   get 1st attempt
#   while not valid:
#       print error
#       get next attempt
#   return result
#
# [+/-]digits.digits
#   optional dign
#   bunch o'digits
#   dot
#   truckload more digits

import string

def isvInt(numstring):
    pos = 0
    if numstring[0] in "+-":
        sign = numstring[0]
        pos += 1
    else:
        sign = "+"
    while pos < len(numstring):
        if numstring[pos] not in string.digits:
            return False
        else: 
            pos += 1
    return True

def getInt(prompt='Enter an integer: ',
            error='Error, invalid input - try again '):
    numstring = raw_input(prompt)
    while not isvInt(numstring):
        print error
        numstring = raw_input(prompt)
    return int(numstring)

def factLoop(n): #4 Demon evil factorial loop.
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def newRaph(n, delta, xold): #5 New Raph .sprt less question
    xnew = (n/xold+xold)/2
    while abs(xnew-xold) > delta:
        xnew = (n/xold+xold)/2
    return xnew

# getInt testing

# if __name__ == '__main__':
#    print getInt('Put in a number ', 'wrong')
    