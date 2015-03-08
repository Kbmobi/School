# given a person's height (metres) and weight (kilograms)
# calculate their Body Mass Index
# BMI = weight(kg)/height(m)2    95.5 kg   

print 'This program will calculate your BMI based off your weight and height in METRIC.'
raw_input('Press any key to continue...')
H = input('Please insert how tall (in METRES) you are: ') #example 1.83m
W = input('Please insert how fat (in KILOGRAMS) you are: ') #example 95.5kg
BMI = W/(H*H)
print '\nHere are the results!\n\nYou have a BMI of: ',BMI,'\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
