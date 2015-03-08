import Util

def eTriangle(n):
    '''
    1. Draw a triangle of asterisks like this:
    *
   ***
  *****
 *******
*********
prompt the user for the size of the longest line - and insist that it is an odd number.
'''
    line = 1
    space = n/2
    ast = 1
    while line <= n/2+1:
        print ' '*space,'*'*ast,' '*space
        space -= 1
        ast += 2
        line += 1

def eDiamond(n):
    '''
    2. Draw a diamond of asterisks:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
again prompt the user for the longest line and insist that it be odd.
'''
    line = 1
    space = n/2
    ast = 1
    while line <= n/2+1:
        print ' '*space,'*'*ast,' '*space
        space -= 1
        ast += 2
        line += 1
    ast -= 4
    space += 2
    while line <= n:
        print ' '*space,'*'*ast,' '*space
        space += 1
        ast -= 2
        line += 1
        
def hSquare(out, inside):
    '''
    3. Draw a hollow square:
*********
*********
*********
***   ***
***   ***
***   ***
*********
*********
*********
prompt the user for the length of the outer side and the length of the inner side (the above example is 9 outer, 3 inner)
'''
    line = 1
    boarder = (out - inside) / 2
    boarder2 = boarder + inside
    while line <= out:
        if line <= boarder:
            print '*'*out
        elif boarder <= line <= boarder2:
            print '*'*boarder+' '*inside+'*'*boarder
        elif line >= boarder2:
            print '*'*out
        line += 1

def dTime(time1, time2):
    '''
4. Accept two times, in 24-hour notation (e.g. 2359 = 1 minute to midnight) 
and then print the time difference. 
    
For example, if time1 = 1215 and time2 = 1436 the difference is 2 hours 21 minutes. 
If time1 = 2230 and time2 = 0415 the difference is 5 hours 45 minutes. 
(Note that the first time entered *is* earlier and that the time may go across midnight.) 
Print the difference as hours and minutes, not a single 4-digit number.
''' 
    ######################
    t1h = int(time1[:2]) # Cuts the strings apart and converts them into ints
    t1m = int(time1[2:]) # in order to alow them for equasions
    t2h = int(time2[:2]) 
    t2m = int(time2[2:]) 
    ######################
    
    if t1h < t2h:
        h = t2h - t1h
    elif t1h > t2h:
        h = 24 + (t2h - t1h)
    elif t1h == t2h and t1m > t2m: # if the hours time1 = time2, but the minutes go backwards
        h = 24 # It sets the hours to 24 to prepare for the minute equasion. 
    
    
    if t1m < t2m:
        m = t2m - t1m
    elif t1m > t2m:
        m = 60 + (t2m - t1m)
        h -= 1
    
    print "The time difference is: ",h,"Hours, and ",m,"Minutes"