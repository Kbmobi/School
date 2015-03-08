import util

def triAst(): #2 Lab04 -- Print a triangle using a loop
    ''' example: 
        n = 3
        *
        **
        ***
'''
    n = util.getInt()
    line = 1
    while line <= n:
        print "*"*line
        line += 1

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    print "Print a triangle of '*'s"
    triAst()
    raw_input()
    