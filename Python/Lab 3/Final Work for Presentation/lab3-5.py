import lab03
import util

if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab03\n\n"
    print "Newton-Raphson square rooting." 
    n = util.getInt("Please input an initial value: ", "error") # any integer.
    delta = util.getFloat("Please input a tolerance (delta): ", "error") #example: 0.00001
    # xold = util.getFloat("Please input your initial approximation(guess): ", "error")
    print lab03.newRaph(n, delta),
    print "is your answer I think."
