import string

def getSymbol(prompt='Enter a single punctuation symbol: ', error='Error'):
    sym = raw_input(prompt)
    if len(sym) != 1: 
        print error
        return getSymbol()
    elif sym in string.punctuation:
        return sym

def isvFloat(numstring):
    pos = 0
    dot = 0
    if numstring[0] in "+-":
        sign = numstring[0]
        pos += 1
    else:
        sign = "+"
    while pos < len(numstring):
        if numstring[pos] not in string.digits:
            if numstring[pos] == string.punctuation[13]: #string.punctuation[13] = "."
                pos += 1
                dot += 1
            else:
                return False
        else: 
            pos += 1
    if dot > 1:
        return False
    else:
        return True

def getFloat(prompt='Enter an number: ',
            error='Error, invalid input - try again '):
    numstring = raw_input(prompt)
    while not isvFloat(numstring):
        print error
        numstring = raw_input(prompt)
    return float(numstring)

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


'''
####################
# Lab 03 Functions #
####################
'''
def nextTen():
    '''
    #1 Integer, printing the 10 numbers after it
    '''
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
    gVar = getSymbol()
    yAxis = N
    pos = 0
    while pos < yAxis:
        print gVar*N
        pos += 1

def pre_select(prompt='Please select an option now: ', error='try again'):
    n = raw_input(prompt)
    if len(n) != 1:
        print error
        pre_select()
    else:
        return int(n)

def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        print " "
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
# ------------------------------------------------------------------------------
def selected_option(n):
    if n == 1:
        print "Input an integer and then print the next 10 numbers."
        nextTen()
        return restart()
    if n == 2: # use 8 and 12 for example to get 4
        print "greatest common divisor of 2 numbers."
        answer = GCD()
        print "The greatest common divisor of your 2 numbers is:",answer,"\n"
        return restart()
    if n == 3: 
        print "the sum of a series of numbers."
        print "###########################################################"
        print "#  the series ends when the user enters a negative number #"
        print "###########################################################"
        answer = stNum()
        print "Your total sum of all numbers is",answer
        return restart()
    if n == 4: # 6 = 720 for example, n! = 6*5*4*3*2*1 = 720
        print "Print that positive number's factorial."
        fact = factLoop()
        print fact,"is your result..."
        return restart()
    if n == 5:
        print "Newton-Raphson square rooting." 
        n = getInt("Please input an initial value: ", "error")
        delta = getFloat("Please input a tolerance (delta): ", "error")
        # xold = getFloat("Please input your initial approximation(guess): ", "error")
        print newRaph(n, delta),
        print "is your answer I think."
        return restart()
    if n == 6:
        print "Print a NxN square of asterisks"
        getGrid()
        return restart()
    if n == 7:
        print "Print a NxN square of user input symbols"
        getGrid2()
        return restart()

#Idiot checking to see if they entered an invalid option.

def idiot_check(n):
    if n > 7:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif n < 1:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif 8 > n > 0:
        print '\nYour input was accepted.\n'
        return selected_option(n)
    else:
        print '\nError #0\n'
        return restart()
    
def start():  # start of the program.
    print "Please select one of the following options:\n"
    print "#1 --  Input an integer and then print the next 10 numbers."
    print "#2 --  Greatest common divisor of 2 numbers."
    print "#3 --  Sum a series of numbers"
    print "#4 --  Print that positive number's factorial."
    print "#5 --  The Newton-Raphson method for calculating square roots."
    print "#6 --  Print a NxN square of asterisks, as (N=5)."
    print "#7 --  Print a NxN square of symbols of your choice."
    print "--------------------------------------------------------------"
    n = pre_select()
    return idiot_check(n) # checks to see if the user is retarded.

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab03\n\n"
    start()
