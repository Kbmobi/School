import fractions
import util
import lab03

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
        lab03.nextTen()
        return restart()
    if n == 2: # use 8 and 12 for example to get 4
        print "greatest common divisor of 2 numbers."
        answer = lab03.GCD()
        print "The greatest common divisor of your 2 numbers is:",answer,"\n"
        return restart()
    if n == 3: 
        print "the sum of a series of numbers."
        print "###########################################################"
        print "#  the series ends when the user enters a negative number #"
        print "###########################################################"
        answer = lab03.stNum()
        print "Your total sum of all numbers is",answer
        return restart()
    if n == 4: # 6 = 720 for example, n! = 6*5*4*3*2*1 = 720
        print "Print that positive number's factorial."
        fact = lab03.factLoop()
        print fact,"is your result..."
        return restart()
    if n == 5:
        print "Newton-Raphson square rooting." 
        n = util.getInt("Please input an initial value: ", "error")
        delta = util.getFloat("Please input a tolerance (delta): ", "error")
        # xold = util.getFloat("Please input your initial approximation(guess): ", "error")
        print lab03.newRaph(n, delta),
        print "is your answer I think."
        return restart()
    if n == 6:
        print "Print a NxN square of asterisks"
        lab03.getGrid()
        return restart()
    if n == 7:
        print "Print a NxN square of user input symbols"
        lab03.getGrid2()
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
