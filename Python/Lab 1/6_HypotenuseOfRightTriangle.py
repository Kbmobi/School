import math
print 'This program will give you the hypotenuse of a right triangle.'
raw_input('Press any key to continue...')
print "\n|\\\n| \\\n|  \\\n|___\\\n<---> = Base"
a = input('Please insert the base: ')
print "|\\    ^\n| \\   |\n|  \\  | = Height\n|___\\ |"
b = input('Please insert the height: ')
c = math.sqrt(a**2+b**2)
print '|\\\n| \\<--- Hypotenuse!\n|  \\\n|___\\\nThe hypotenuse of the right triangle is',("%.3f"%c),'squared!\n\nThank you for using my program.\n\nKeegan Bailey\nC0369801'
