#Comp 112 Lab 2 - Keegan Bailey 11/10/2012 (Python 2.7.3)
#In this lab I used Function, Lists, If Statements.
 
#importing needed modules for lab 02
import time
import math

#Function for restarting the script once an option is completed, or a predictable error is discovered.
def restart(): #Made for restarting the program.
    answer = raw_input("Do you want to restart this program? ")
    if answer.strip() in "y Y yes Yes YES".split():
        return start()
    else:
        print '\n\nThank you for using my program.\n\nKeegan Bailey'

# ----------------------------------------------------------------------------------------
# All the math and calculations for the 17 Lab 02 questions are in this block of functions
def c2f(n): #1 Celsius to Fahrenhiet
    n = n*(9.0/5)+32
    return n

def f2c(n): #2 Farenhiet to Celsius
    n =(n-32)*(5/9.0)
    return n
    
def AofSq(n): #3 Area of a quare
    n = n**2
    return n
    
def AofRec(L, W): #4 Area of Rectangle
    A = L*W
    return A

def AofRTriangle(B, H): #5 Area of Right Triangle
    A = (B*H)/2
    return A
    
def HypOfRTriangle(B, H): #6 Hypot of Right Triangle
    A = math.sqrt(B**2+H**2)
    A = round(A,3)
    return A

def CircOfCircle(n): #7 Circumference of a Circle
    pi = math.pi
    n = 2*pi*n
    n = round(n,3)
    return n

def AreaOfCircle(n):#8 Area of Circle
    pi = math.pi
    n = pi*n**2
    n = round(n,3)
    return n

def FractionToDecimal(N, D): #9 Fraction to Decimal
    N = float(N)
    D = float(D)
    X = N/D
    return X

def Average(n1, n2, n3): #10 Average of 3 numbers
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n = (n1+n2+n3)/3
    n = round(x,3)
    return n

def SumProductRemainder(n1, n2): #11 Sum, Product, and Remainder of 2 numbers
    n1 = float(n1)
    n2 = float(n2)
    x = (n1+n2)
    x2 = (n1*n2)
    x3 = (n1 % n2)
    n = [x, x2, x3]
    return n

def Journey(km, km2, L, L2): #12 fuel consumed, and your average consumption rate
    km = float(km)
    km2 = float(km2)
    km3 = km2-km
    L = float(L)
    L2 = float(L2)
    L3 = L-L2
    L3 = float(L3)
    d = L3/km3
    d = float(d)
    d = round(d,3)
    n = [L3, d]
    return n

def CND2USD(n): #13 Curency Conversion 
    USD = 1.0181
    n = n*USD
    return n
    
def BMI(H, W): #14 calculate your BMI
    BMI = W/(H*H)
    return BMI

def HullSpeed(n): #15 Hull speed of a boat based off length
    K = 1.35*(n**0.5)
    K = round(K,3)
    return K

def GasBill(first, final, days): #16 Gas Bill
    first = float(first)
    final = float(final)
    gas = final-first
    dcost = days*9.02/100
    gcost = gas*1.433/100
    hcost = (((days*9.02)+(gas*1.433))*0.12)/100
    bill = (((days*9.02)+(gas*1.433))*1.12)/100
    dcost = round(dcost,2)
    gcost = round(gcost,2)
    hcost = round(hcost,2)
    bill = round(bill,2)
    L = [dcost, gcost, hcost, bill]
    return L
  
def Morgage(P, rate, years): #17 Morgage Rates
    R = (rate/100)/12
    T = years*12
    A = (P*R*((R+1)**T))/(((R+1)**T)-1)
    A = round(A,2)
    x = [P, R, T, A]
    return x

# ----------------------------------------------------------------------------------------------------
# Lab 2 questions are in this function. All 17 questions have their input and print's in this function
def selected_option(n):
    if n == 1:
        print 'Converting Celsius to Fahrenheit.'
        raw_input('Press enter to continue...')
        n = input('Please insert Celsius temperature: ')
        print c2f(n),'degrees Fahrenheit!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 2:
        print 'Converting Fahrenheit to Celcius.'
        raw_input('Press enter to continue...')
        n = input('Please insert Fahrenheit temperature: ')
        print round(f2c(n),2),'degrees Celcius!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 3:
        print 'Calculating area of a square.'
        raw_input('Press enter to continue...')
        n = input('Please insert the side\'s length: ')
        print 'The area of the rectangle is',AofSq(n),'squared!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 4:
        print 'Calculating area of a rectangle.'
        raw_input('Press enter to continue...')
        L = input('Please insert the length: ')
        W = input('Please insert the width: ')
        print 'The area of the rectangle is',AofRec(L, W),'squared!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 5:
        print 'This program will give you the area of a right triangle.'
        raw_input('Press enter to continue...')
        print "\n|\\\n| \\\n|  \\\n|___\\\n<---> = Base"
        B = input('Please insert the base: ')
        print "|\\    ^\n| \\   |\n|  \\  | = Height\n|___\\ |"
        H = input('Please insert the height: ')
        print 'The area of the right triangle is',AorRTriangle(B, H),'squared!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 6:
        print 'This program will give you the hypotenuse of a right triangle.'
        raw_input('Press enter to continue...')
        print "\n|\\\n| \\\n|  \\\n|___\\\n<---> = Base"
        B = input('Please insert the base: ')
        print "|\\    ^\n| \\   |\n|  \\  | = Height\n|___\\ |"
        H = input('Please insert the height: ')
        print '|\\\n| \\<--- Hypotenuse!\n|  \\\n|___\\\nThe hypotenuse of the right triangle is:',HypOfRTriangle(B, H),'!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 7:
        print 'This program will give you the circumference of a circle.'
        raw_input('Press enter to continue...')
        n = input('Please insert the radius: ')
        print 'The circumference of the circle is:',CircOfCircle(n),'!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 8:
        print 'This program will give you the area of a circle.'
        raw_input('Press any key to continue...')
        n = input('Please insert the radius: ')
        print 'The area of the circle is',AreaOfCircle(n),'!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 9:
        print 'This program will convert a fraction to a decimal.'
        raw_input('Press enter to continue...')
        N = input('Please insert the numerator (top number): ')
        D = input('Please insert the denominator (bottom number): ')
        print 'The decimal is',FractionToDecimal(N, D),'!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 10:
        print 'This program will give you the average of 3 numbers.'
        raw_input('Press enter to continue...')
        n1 = input('Please insert the 1st number: ')
        n2 = input('Please insert the 2nd number: ')
        n3 = input('Please insert the 3rd number: ')
        print 'The average is',Average(n1, n2, n3),'!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 11:
        print 'This program will calculate two numbers. It will give you sum, product, and the remainder of the first divided by the second.'
        raw_input('Press enter to continue...')
        n1 = input('Please insert the 1st number: ')
        n2 = input('Please insert the 2nd number: ')
        print 'Here are the results!\n\nSum: ',SumProductRemainder(n1, n2)[0],'\nProduct:',SumProductRemainder(n1, n2)[1],'\nRemainder of the 2 numbers devided is:',SumProductRemainder(n1, n2)[2]
        raw_input('Press enter to continue...')
        return restart()
    elif n ==12:
        print 'This program will calculate how much fuel you consumed, and your average consumption on your journey.'
        raw_input('Press enter to continue...')
        km = input('Please insert your kilometers at the START of the journey: ')
        km2 = input('Please insert your kilometers at the END of your journey: ')
        L = input('Please insert how many litres of gas you had at the START of your journey: ')
        L2 = input('Please insert how many litres of gas you had at the END of your journey: ')
        print 'Here are the results!\n\nYou consumed',Journey(km, km2, L, L2)[0],'litres of gas!\nYour average consumption was',Journey(km, km2, L, L2)[1],'litres per Km!'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 13:
        print 'This program will convert Canadian curency to US at the current exchange rate.\n(1 Canadian dollar = 1.0181 US dollars) <- LOL USA'
        raw_input('Press enter to continue...')
        n = input('Please insert how many Canadian currency you have: ')
        print '\nHere are the results!\n\nYou have $',CND2USD(n),'USD'
        raw_input('Press enter to continue...')
        return restart()
    elif n == 14:
        print 'This program will calculate your BMI based off your weight and height in METRIC.'
        raw_input('Press any key to continue...')
        H = input('Please insert how tall (in METRES) you are: ') #example 1.83m
        W = input('Please insert how fat (in KILOGRAMS) you are: ') #example 95.5kg
        print 'Here are the results!\n\nYou have a BMI of:',BMI(H, W)
        raw_input('Press enter to continue...')
        return restart()
    elif n == 15:
        print 'This program will calculate the hull speed (in knots) of your boat based off the length.'
        raw_input('Press any key to continue...')
        n = input('Please insert how length of your boat (in FEET): ') #example 120
        print '\nHere are the results!\n\nYou have a hull speed of: ',HullSpeed(n)
        raw_input('Press enter to continue...')
        return restart()
    elif n == 16:
        print 'This program will calculate and print a bill based off meter reading against days (I think).'
        raw_input('Press any key to continue...')
        first = input('Please input your first meter reading in cubic meters: ') #example 45
        final = input('Please input your final meter reading in cubic meters: ') #example 678
        days = input('Please input how many days it has been: ') #example 30
        print 'Here are the results!\n\n  Day Cost: $',GasBill(first, final, days)[0],'\n  Gas Cost: $',GasBill(first, final, days)[1],'\n  HST 12%: $',GasBill(first, final, days)[2],'\n ------------------ \n  Total Cost: $',GasBill(first, final, days)[3],"\n"
        raw_input('Press enter to continue...')
        return restart() 
    elif n == 17:
        print 'This program will calculate your monthly morgage intrest rates.'
        raw_input('Press Enter to continue...')
        P = input('Please insert your initial principal (loan ammount) without the "$" sign: ') #example $20,000
        rate = input('Please insert your annual intrest rate as a percentage without the "%" sign: ') #7.5
        years = input('Please insert how many years are in your amortization period: ') #Example 5 years
        print '\nHere are the results!\n\nLoan Ammount: $',Morgage(P, rate, years)[0],'\nIntrest Rate: %',Morgage(P, rate, years)[1],'\nNumber of Payments: #',Morgage(P, rate, years)[2],'\n\nYou have a monthly ammount of: $',Morgage(P, rate, years)[3],'\n'
        raw_input('Press enter to continue...')    
        return restart()
    else:
        print 'You have encountered an error.\nPlease make sure you selected a valid option.\n\n\n'
        time.sleep(1)
        return restart()
#
#Idiot checking to see if they entered an invalid option.
#
def idiot_check(n):
    if n > 17:
        print 'You did not input a valid number, please try again.\n\n\n'
        time.sleep(1)
        return restart()
    elif n < 1:
        print 'You did not input a valid number, please try again.\n\n\n'
        time.sleep(1)
        return restart()
    elif 18 > n > 0:
        print '\nYour input was accepted.\n'
        time.sleep(1)
        return selected_option(n)
    else:
        print '\nerror\n'
        time.sleep(2)
        return restart()
    
def start():  # start of the program. first def to be run
    print "#1 --  Convert Celsius to Fahrenheit."
    print "#2 --  Convert Fahrenheit to Celsius."
    print "#3 --  Calculate the Area of a Square."
    print "#4 --  Calculate the Area of a Rectangle."
    print "#5 --  Calculate the Area of a Right Angled Triangle."
    print "#6 --  Calculate the Hypotenuse of a Right Angled Triangle."
    print "#7 --  Calculate the Circumference of a Circle."
    print "#8 --  Calculate the Area of a Circle."
    print "#9 --  Convert a Fraction to a Decimal."
    print "#10 -  Calculate the Average of 3 Numbers."
    print "#11 -  Calculate 2 Numbers, give Sum, Product, & Remainder."
    print "#12 -  Calculate Fuel Consumption and Average on Journey."
    print "#13 -  Convert Canadian Currency to US."
    print "#14 -  Calculate your BMI in metric."
    print "#15 -  Calculate the Hull Speed of a Boat."
    print "#16 -  Calculate a Gas Bill."
    print "#17 -  Calculate a Mortgage's Intrest."
    print "--------------------------------------------------------------"
    n = input('Please select an option now: ') 
    return idiot_check(n) # checks to see if the user is retarded.

# If statement to start the script
if __name__ == '__main__':
    print "Keegan Bailey\nC0369801\nComp112 -- Lab02\n\n"
    print "Please select one of the following options:\n"
    time.sleep(0.5)
    start()
