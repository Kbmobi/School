# given the kilometrage at the start of a journey,
# the Km at the end, the amount of fuel in the car's
# tank at the beginning and end (in litres), calculate
# the amount of fuel used and the average consumption (Litres/Km)

print 'This program will calculate how much fuel you consumed, and your average consumption on your journey.'
raw_input('Press any key to continue...')
km = input('Please insert your kilometers at the START of the journey: ')
km = float(km)
km2 = input('Please insert your kilometers at the END of your journey: ')
km2 = float(km2)
km3 = km2-km
L = input('Please insert how many litres of gas you had at the START of your journey: ')
L = float(L)
L2 = input('Please insert how many litres of gas you had at the END of your journey: ')
L2 = float(L2)
L3 = L-L2
L3 = float(L3)
d = L3/km3
d = float(d)
print '\nHere are the results!\n\nYou consumed',L3,'litres of gas!\nYour average consumption was',round(d,3),'litres per Km!''\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
