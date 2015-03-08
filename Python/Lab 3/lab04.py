import fractions
import string

################################################################################
# Lab 03 Functions
################################################################################
def nextTen(): #1 Integer, printing the 10 numbers after it
    num = getInt()
    x = 1
    print "Numbers after",num,":\n--------"
    while x <= 10:
        num += 1
        print x,":",'\t',num
        x += 1

def GCD(): #2 greatest common divisor
    num1 = getInt('Please input 1st integer: ', 'Try Again')
    num2 = getInt('Please input 2st integer: ', 'Try Again')
    while num1 < 1 or num2 < 1:
            print "Start over--do not use negative numbers!"
            return gcd()
    return fractions.gcd(num1, num2)

def stNum(): #3 Sum of a series of numbers.
    x = 0
    num2 = 0
    stop = 0
    while stop <= 1:
        num =  getInt()
        if num < 0:
            print "stopping program"
            stop = 1
            return num2
        else:
            x += 1
            num2 += num
            print "Series #",x,"\tTotal:",num2

def factLoop(): #Lab03 -- #4 Demon evil factorial loop.
    n = getInt()
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def newRaph(n, delta): #Lab03 -- #5 New Raph .sprt less question
    xold = n/2.0
    xnew = (n/xold+xold)/2.0
    while abs(xnew-xold) > delta:
        xold = xnew
        xnew = (n/xold+xold)/2.0
    return xnew

def getGrid(): #Lab03 -- #6 Printing a NxN grid of *'s
    N = getInt()
    yAxis = N
    pos = 0
    while pos < yAxis:
        print "*"*N
        pos += 1
        
def getGrid2(): #Lab03 -- #6 Printing a NxN grid of user created variables
    N = getInt()
    gVar = "Put in anything you want to be in a grid: "
    yAxis = N
    pos = 0
    gVar = raw_input(gVar)
    while pos < yAxis:
        print gVar*N
        pos += 1
##################################################################################