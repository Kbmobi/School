import util

def triAst2(n, line): #3 Lab04 -- Print a triangle using recursion
    ''' example:
        n = 3
        *
        **
        ***
'''
    if line <= n:
        print "*"*line
        line += 1
        return triAst2(n, line)

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab04\n\n"
    print "Print a triangle of '*'s (recursive)"
    n = util.getInt()
    line = 1
    triAst2(n, line)
    raw_input()
