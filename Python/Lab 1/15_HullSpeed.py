# given the length of a boat, calculate the hull speed
# Hull Speed (knots) = 1.35 * Length0.5

print 'This program will calculate the hull speed (in knots) of your boat based off the length.'
raw_input('Press any key to continue...')
L = input('Please insert how length of your boat (in FEET): ') #example 120
L = float(L)
K = 1.35*(L**0.5)
print '\nHere are the results!\n\nYou have a hull speed of: ',round(K,3),'knots\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
