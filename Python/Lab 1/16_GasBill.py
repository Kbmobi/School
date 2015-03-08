# A customer's gas bill is calculated by adding a standard charge
# of 9.02 cents per day to the charge for gas, calculated as 1.433
# cents per cubic metre. The whole bill is then liable for HST (thank you Gordon!)
# at 12%. Write a program that reads the number of days,
# and the initial and final meter readings (in cubic metres), and calculates and prints the bill.
# ((days*9.02)+(1.433*gas))*12%=

print 'This program will calculate and print a bill based off meter reading against days (I think).'
raw_input('Press any key to continue...')
first = input('Please input your first meter reading in cubic meters: ') #example 45
first = float(first)
final = input('Please input your final meter reading in cubic meters: ') #example 678
final = float(final)
gas = final-first
hst = 1.12
days = input('Please input how many days it has been: ') #example 30
dcost = days*9.02
gcost = gas*1.433
hcost = ((days*9.02)+(gas*1.433))*0.12
bill = ((days*9.02)+(gas*1.433))*1.12
print '\nHere are the results!\n\n  Day Cost: $',round(dcost,2),'\n  Gas Cost: $',round(gcost,2),'\n  HST 12%: $',round(hcost,2),'\n ------------------ \n  Total Cost: $',round(bill,2),'\n\n\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
