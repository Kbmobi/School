import string

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

def getGrid(n, var): #1 -- Lab 04 -- Print a NxN square of whatever while using nexted loop.
    yAxis = n
    xAxis = n
    r = 0 # value that sets the line
    while r < yAxis: # controls what line it's printing on
        c = 0 # resets the variable to 0 again after every loop
        while c < xAxis: # while loop for actually printing the line
            print var, # var, waits untill the next print statment to dump all prints
            c += 1 # when column hits "n" it will break loop
        print # dumps line of prints
        r += 1 #once this hits the "n" it will stop looping

# I had to use the nots for reference, commented every step to show understanding on what it did. Still confusing as fuck
# and way more difficult compaired to string*number for making blocks.

def triAst(): #2 Lab04 -- Print a triangle using a loop
    n = getInt()
    line = 1
    while line <= n:
        print "*"*line
        line += 1
        
def triAst2(n, line): #3 Lab04 -- Print a triangle using recursion
    if line <= n:
        print "*"*line
        line += 1
        return triAst2(n, line)
    
def triAst3():  #4 Lab04 -- Print an upside down triangle
    n = getInt()
    line = n
    space = " "
    sd = 0
    while line > 0:
        print space*sd,line*'*'
        sd += 1
        line -= 1

#5 value of e = lim (1+1/h)
def factLoop(var): #Lab03 -- #4 Demon evil factorial loop.
    res = 1
    while var > 1:
        res *= var
        var -= 1
    return res

def vE(n): # n! = n * (n-1) * (n-2) * ... * 1
    var = 1 # Sets the default variable to use throughout the loop
    stop = n # Sets stop to the number sents in through the argument.
             #It's reset to stop because the number will change often
    e = 1   #Sets e to 1, e always starts @ 1
    while var <= stop: # Loops until Var is les then or equal to stop(starting input)
        e = e+(1.0/factLoop(var)) #function to create a new e for printing,
        '''and uses e+1/n!. n! is done by factiorial loop, so the more you want to
loop, the higher the factorial will get, it will start at 1, and go from there
1, 2, 6, 24, 120, 720, 5040, 40320 | Factiorials function as follows: Factorial of
5 for example is 5*4*3*2*1=120
'''
        print "Loop #",var,"\t=\t",e # prints once per loop with 2 variables. 
        var += 1
        
def printMultiples(n, length, col):
    if col <= length:
        print n*col, '\t', 
        col += 1
        return printMultiples(n, length, col)
    else:
        print
    
def printMultTable(i, length):
    if i <= length:
        col = 1
        printMultiples(i, length, col)
        i += 1
        return printMultTable(i, length)

def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        print " "
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'

def selected_option(n):
    if n == 1:
        print "Print a NxN square of whatever while using nexted loop."
        n = getInt()
        var = raw_input('Please input a variable: ')
        getGrid(n, var)
        return restart()
    if n == 2: 
        print "Print a triangle of '*'s"
        triAst()
        return restart()
    if n == 3:
        print "Print a triangle of '*'s"
        n = getInt()
        line = 1
        triAst2(n, line)
        return restart()
    if n == 4:
        print "Print a triangle of '*'s upside down"
        triAst3()
        return restart()
    if n == 5:
        print "Prompt for the number of terms to use and then calculate the value of e"
        n = getInt()
        vE(n)
        return restart()
    if n == 6:
        length = getInt('input a number for the multTable length: ', 'YOU DUN GOOFd')
        i = 1
        printMultTable(i, length)
        return restart()

#Idiot checking to see if they entered an invalid option.

def idiot_check(n):
    if n > 8:
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
    print "#1 --  Print a NxN square of whatever while using nexted loop."
    print "#2 --  Triangle of asterisks. (loop)"
    print "#3 --  Triangle of asterisks. (rec)"
    print "#4 --  Triangle of asterisks. (upside down)"
    print "#5 --  Calculate the value of e"
    print "#BONUS -- Print multTable using recursion"
    print "--------------------------------------------------------------"
    n = input('Please select an option now: ') 
    return idiot_check(n) # checks to see if the user is retarded.

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    start()
