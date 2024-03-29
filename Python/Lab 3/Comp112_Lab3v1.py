import fractions
import util

def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'

def option1(num): #1 Integer, printing the 10 numbers after it
    x = 1
    print "Numbers after",num,":\n--------"
    while x != 11:
        num += 1
        print x,":",'\t',num
        x += 1
    return restart()
        
def floatCorrect(num): #1 float correction
    numFixed = int(num)
    print num,'is now',numFixed
    num = numFixed
    return option1(num)
        
def GCD(num1, num2): #2 greatest common divisor
    num1 = int(num1)
    num2 = int(num2)
    return fractions.gcd(num1, num2)

def stNum(): #3 Sum of a series of numbers.
    x = 0
    num2 = 0
    stop = 0
    while stop != 1:
        num = raw_input('Please input a number: ')
        if str.isdigit(num):
            num = int(num)
            x += 1
            num2 += num
            print "Series #",x,"\tTotal:",num2
        elif num[0] == "-":
            print "stopping program"
            stop = 1
            return num2
    return restart()
    
def fact_loop(n): #4 Demon evil factorial loop.
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
    

# ------------------------------------------------------------------------------
# str.isdigit()

def selected_option(n):
    if n == 1:
        print "Input an integer and then print the next 10 numbers."
        num = input('Please input an integer: ')
        if num == type(int) and num > 0:
            print "you number",num,"was accepted"
            return option1(num)
        elif num == float(num) and num > 0:
            print "A float is not an integer, so let me fix that for you."
            return floatCorrect(num)
        elif num == num < 0:
            print "Your number can not be negative. I am just going to pretend you put a '-' in by mistake."
            num = num * -1
            return option1(num)
        else:
            print "error"
            return restart()
    if n == 2:
        print "greatest common divisor of 2 numbers."
        num1 = raw_input('Please input your first possitive integer: ')
        num2 = raw_input('Please input your second possitive integer: ')
        if str.isdigit(num1) and str.isdigit(num2):
            print "Both numbers are possitive, and they were accepted"
            print "The greatest common divisor of your 2 numbers is:",GCD(num1, num2)
            return restart()
        else:
            print "You apparently can't read! Try again..."
            return selected_option(2)
    if n == 3:
        print "the sum of a series of numbers."
        print "###########################################################"
        print "#  the series ends when the user enters a negative number #"
        print "###########################################################"
        print stNum(),
        print "is your total sum."
        return restart()
    if n == 4:
        print "Print that positive number's factorial."
        n = input("Please input a positive number: ")
        print fact_loop(n),
        print "is your result..."
        return restart()
    if n == 5:
        print "Newton-Raphson square rooting." # 
        n = input("Please input an initial value: ")
        delta = input("Please input a tolerance (delta): ")
        xold = input("Please input your initial approximation(guess): ")
        xold = float(xold)
        print newRaph(n, delta, xold),
        print "is your answer I think."
        return restart()
        
        
                    
            
#
#Idiot checking to see if they entered an invalid option.
#
def idiot_check(n):
    if n > 7:
        print 'You did not input a valid number, please try again.\n\n\n'
        return restart()
    elif n < 1:
        print 'You did not input a valid number, please try again.\n\n\n'
        return restart()
    elif 8 > n > 0:
        print '\nYour input was accepted.\n'
        return selected_option(n)
    else:
        print '\nError #0\n'
        return restart()
    
def start():  # start of the program.
    print "#1 --  Input an integer and then print the next 10 numbers."
    print "#2 --  Greatest common divisor of 2 numbers."
    print "#3 --  Sum a series of numbers"
    print "#4 --  Print that positive number's factorial."
    print "#5 --  The Newton-Raphson method for calculating square roots."
    print "#6 -- "
    print "--------------------------------------------------------------"
    n = input('Please select an option now: ') 
    return idiot_check(n) # checks to see if the user is retarded.

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab03\n\n"
    print "Please select one of the following options:\n"
    start()
