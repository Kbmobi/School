import util

def triAst3():  #4 Lab04 -- Print an upside down triangle
    ''' example
        n = 3
        ***
         **
          *
'''
    n = util.getInt()
    line = n
    space = " "
    sd = 0
    while line > 0:
        print space*sd,line*'*'
        sd += 1
        line -= 1

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    print "Print a triangle of '*'s upside down"
    triAst3()
    raw_input()