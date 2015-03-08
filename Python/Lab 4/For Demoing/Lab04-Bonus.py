import util

def printMultiples(n, length, col):
    ''' this function controls the print of numbers on the screen.
numbers do not go past the length value when printing. 
'''
    if col <= length:  
        print n*col, '\t', 
        col += 1
        return printMultiples(n, length, col)
    else:
        print
    
def printMultTable(i, length):
    ''' Recursive conversion of the multTable function included within Ch6 of
the classroom notes. They are under the section "Encapsulation and generalization"
for further documentation.

http://http://turing.cs.camosun.bc.ca/COMP112/notes/HttC/ch6.html
'''
    if i <= length:
        col = 1
        printMultiples(i, length, col) #function to print numbers on screen
        i += 1
        return printMultTable(i, length)

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    print "Print the multiplication table!"
    length = util.getInt('To what number do you want the table to print to: ', 'unacceptable')
    i = 1 # i = 1 needs to stay out of the function and be fed in as an argument
    printMultTable(i, length)
    raw_input()
