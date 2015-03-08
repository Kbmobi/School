import util

def restart(): #Made for restarting the program.
    print "\n"
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        print " "
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
        raw_input()

# Functions Start

def eTriangle(n):
    '''
    1. Draw a triangle of asterisks like this:
    *
   ***
  *****
 *******
*********
prompt the user for the size of the longest line - and insist that it is an odd number.
'''
    line = 1
    space = n/2
    ast = 1
    while line <= n/2+1:
        print ' '*space,'*'*ast,' '*space
        space -= 1
        ast += 2
        line += 1

def eDiamond(n):
    '''
    2. Draw a diamond of asterisks:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
again prompt the user for the longest line and insist that it be odd.
'''
    line = 1
    space = n/2
    ast = 1
    while line <= n/2+1:
        print ' '*space,'*'*ast,' '*space
        space -= 1
        ast += 2
        line += 1
    # Code to clean out the middle area before the 2nd loop
    ast -= 4
    space += 2
    
    while line <= n:
        print ' '*space,'*'*ast,' '*space
        space += 1
        ast -= 2
        line += 1
        
def hSquare(out, inside):
    '''
    3. Draw a hollow square:
*********
*********
*********
***   ***
***   ***
***   ***
*********
*********
*********
prompt the user for the length of the outer side and the length of the inner side (the above example is 9 outer, 3 inner)
'''
    line = 1
    boarder = (out - inside) / 2
    boarder2 = boarder + inside
    while line <= out:
        if line <= boarder:
            print '*'*out
        elif boarder <= line <= boarder2:
            print '*'*boarder+' '*inside+'*'*boarder
        elif line >= boarder2:
            print '*'*out
        line += 1

def dTime(time1, time2):
    '''
4. Accept two times, in 24-hour notation (e.g. 2359 = 1 minute to midnight) 
and then print the time difference. 
    
For example, if time1 = 1215 and time2 = 1436 the difference is 2 hours 21 minutes. 
If time1 = 2230 and time2 = 0415 the difference is 5 hours 45 minutes. 
(Note that the first time entered *is* earlier and that the time may go across midnight.) 
Print the difference as hours and minutes, not a single 4-digit number.
''' 
    ######################
    t1h = int(time1[:2]) # Cuts the strings apart and converts them into ints
    t1m = int(time1[2:]) # in order to alow them for equasions
    t2h = int(time2[:2]) 
    t2m = int(time2[2:]) 
    ######################
    
    #Part 1 to check time
    if t1h < t2h:
        h = t2h - t1h
    elif t1h > t2h:
        h = 24 + (t2h - t1h)
    elif t1h == t2h and t1m > t2m: # if the hours time1 = time2, but the minutes go backwards
        h = 24 # It sets the hours to 24 to prepare for the minute equasion. 
  
    #Part 2 to check minutes
    if t1m < t2m:
        m = t2m - t1m
    elif t1m > t2m:
        m = 60 + (t2m - t1m)
        h -= 1
    
    #Print statment
    print "The time difference is: ",h,"Hours, and ",m,"Minutes"
        
def tDivPrime(n):
    '''
Trial division is the simplest test for primality. It is based on the definition of a prime number. 
A number is prime if it has no divisors other than itself and one.

#2 Let n be the number you want to test.

#3 Divide n by 2. If the result is an integer, then n is not prime because 2 is a factor of n. 
Look at the last digit and if it's an even number, it's divisible by 2. If not, continue.

#4 Divide n by 3. If the result is an integer, then n is not prime because 3 is a factor of n. If not, continue.

#5 Continue dividing n by each number between 2 and n1/2 inclusive. 
If any of them divide evenly, then n is not prime because you found a factor. 
If n has no factors less than its square root, then n is prime. 
'''        
    x = 2
    while x < n:
        if n % x == 0:
            print '\nSo',n,'is most likley  not prime'
            x = n
            return
        else:
            x += 1
    print "\napparently",n,"is prime" 

def padFun(n):
    '''
Accept an input integer N and then print out a table of the numbers 1 to N, together 
with an indication of whether each number in the table is perfect, abundant or deficient.
'''
    stop = 1 # first in to start the count, but also stops when = to input
    while stop <= n:
        div = [1] # list containing 1, because 1 /'s into everything
        pos = 0
        x = 2
        while x < stop:
            if stop % x == 0: # takes the modulus of stop vs every number < stop
                div += [x] # adds those numbers to a list 
            x += 1
            
# get the list ready for addition, and adds all the nodulus numbers together withing the list 
        s = len(div) # Gets the length of the list
        p = 0 # sets p to 0 to avoid errors, and to get ready for addition
        while pos < s:
            p += div[pos]
            pos += 1
            
# if block to check if the number is perfect, abundant, or deficient.            
# 6 is perfect
# 6 = 1+2+3
        if stop == p:
            print stop,"is a perfect number!"
# 12 is abundant
# 12 < 1+2+3+4+6
        elif stop < p:
            print stop,"is abundant!"
# 9 is deficient
# 9 > 1+3
        elif stop > p:
            print stop,"is deficient!"
        stop += 1

# Functions End!


# Function for selected menu options

def selected_option(n):
    if n == 1:
        n = util.getInt('input the length of the bottom side: ', 'invalid option')
        if n > 0:
            if n % 2 == 1:
                eTriangle(n)
                return restart()
            else:
                print "Odd numbers only please!\n"
                return selected_option(1)
        else:
            print 'You know that will not work!'
            return restart()
    if n == 2:
        n = util.getInt('input the length of the middle of the diamond: ', 'invalid option')
        if n > 0:
            if n % 2 == 1:
                eDiamond(n)
                return restart()
            else:
                print "Odd numbers only please!\n"
                return selected_option(2)
        else:
            print 'You know that will not work!'
            return restart()
    if n == 3:
        out = util.getInt('input the length of the outside square: ', 'error')
        inside = util.getInt('input the length of the inside square: ', 'error')
        if out % 2 == inside % 2:
            hSquare(out, inside)
            return restart()
        else:
            print "lobsided square will be printed. Try again please. \n"
            return selected_option(3)
    if n == 4:
        print 'Use 24hr notation, example 3:00 PM = 1500 and 1:30AM = 130.'
        time1 = util.getTime()
        time2 = util.getTime()
        dTime(time1, time2)
        return restart()
    if n == 5:
        print '/------------------------------\\'
        print '|           METHODS            |'
        print '\\------------------------------/'
        print '*                              *'
        print '*     #1 -- Trial division     *'
        print '*     #2 -- Miller-Rabin       *'
        print "* #3 - Fermat's Little Theorem *"
        print '*                              *'
        print '********************************\n\n'
        x = util.getInt('What method would you like to try?: ', 'error')
        if 3 < x < 0:
            print 'invalid option\n'
            selected_option(5)
        else:
            print "\n\n"
            n = util.getInt('What number do you want to check?: ', 'error')
            if x == 1:
                tDivPrime(n)
            else:
                print '\nI was going to do this, but then I realized I just really wanted to make another menu, so you get Trial division'
                tDivPrime(n)
        return restart()
    if n == 6:
        n = util.getInt()
        padFun(n)
        return restart()

    
#Idiot checking to see if they entered an invalid option.

def idiot_check(n):
    if n > 7:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif n < 0:
        print '\nYou did not input a valid number, please try again.\n\n\n'
        return restart()
    elif 7 > n > 0:
        print '\n\n'
        return selected_option(n)
    elif n == 0:
        print "\nGood Bye!~"
    else:
        print '\nError #0\n'
        return restart()
    
# Starting menu function
def start():  
    print "\nPlease select one of the following options:\n"
    print "/--------------------------------------------\\"
    print "| #1 --  Print an Isosceles Triangle of *'s. |"
    print "| #2 --  Print a Diamond of *'s.             |"
    print "| #3 --  Print a hallow square with *'s.     |"
    print "| #4 --  Print difference between 2 times.   |"
    print "| #5 --  Prime number checker.               |"
    print "| #6 --  Use the 'P. A. D.' function         |"
    print "|                                            |"
    print "| #0 --  Quit.                               |"                          
    print "\\--------------------------------------------/"
    print "\n\n"
    n = util.getInt('Please select an option now: ', 'error') 
    return idiot_check(n) # checks to see if the user is retarded.

# Start of the program
if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab05\n\n"
    print "__  _                          \n\ \| |___  ___  _ __  _ __   __ _  \n \ ` / _ \/ _ \| '_ \| '_ \ / _` | \n / . \__  \__  | |_) | |_) | | | | \n/_/|_|___/|___/| .__/|_.__/|_| |_| \n                \___|              \n  ____       _ _                   \n ( __ |_ __ (_| |___  _   _        \n / _  | '_ \| | / _ \| | | |       \n| (_| | |_) | | \__  | |_| |       \n \____|_.__/|_|_|___/| .__/        \n                      \___|   "
    start()
