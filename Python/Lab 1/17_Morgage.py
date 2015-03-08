# given an amount of money, an annual interest rate and an amortization period
#(in years), calculate monthly mortgage payments
#
# Monthly payment = (P * R * (1 + R)**T) / ((1 + R)**T - 1)
# where P = Principal, R= Interest rate (monthly), T = Term (months)

print 'This program will calculate your monthly morgage intrest rates.'
raw_input('Press Enter to continue...')
P = input('Please insert your initial principal (loan ammount) without the "$" sign: ') #example $20,000
rate = input('Please insert your annual intrest rate as a percentage without the "%" sign: ') #7.5
rate = float(rate)
R = (rate/12)/100
years = input('Please insert how many years are in your amortization period: ') #Example 5 years
T = years*12
A = (P*R*(R+1)**T)/((R+1)**T-1)
print '\nHere are the results!\n\nLoan Ammount: $',P,'\nIntrest Rate: %',R,'\nNumber of Payments: #',T,'\n\nYou have a monthly ammount of: $',round(A,2),'\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
