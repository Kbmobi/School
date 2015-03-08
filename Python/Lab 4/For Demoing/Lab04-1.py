import util

def getGrid(n, var): #1 -- Lab 04 -- Print a NxN square of whatever while using nexted loop.
    ''' n = user input for length of cube
        r = value that sets the line, and resets once it hits n.
        c = resets the variable to 0 after every loop, and breaks the 2nd loop.       
'''
    r = 0 # value that sets the line
    while r < n: # controls what line it's printing on
        c = 0 # resets the variable to 0 again after every loop
        while c < n: # while loop for actually printing the line
            print var, # var, waits untill the next print statment to dump all prints
            c += 1 # when column hits "n" it will break loop
        print # dumps line of prints
        r += 1 #once this hits the "n" it will stop looping

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    print "Print a NxN square of whatever while using nexted loop."
    n = util.getInt('Input a length: ', 'error')
    var = util.getSymbol()
    getGrid(n, var)
    raw_input()