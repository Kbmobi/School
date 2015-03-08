#! /usr/bin/python
'''
Thread spawning program that uses an user imput variable to control how many are created.
Threads are delayed by a random number based off the system time using random.seed().
Threads are printed off with a print statment containing the thread number and delay time.
Mutex's are used to control the threads, and make they not overlap in a giant mess.
Once all the threads are done, they program will stop.

I am using the build in librarys of thread, time, and random; however, I am also
using my own personal library util to check input numbers are valid.

By: Keegan Bailey C0369801
'''


import thread, time, random, util

def counter(myId, count):
    '''
    This function to controls newly created threads, manage mutex
    locks, and change the childStatus[] list from 0's to 1's for
    the ability to stop the program. 
'''
    global childStatus
    time.sleep(count) #picks a random number between 1 & 20
    m.acquire() # enables the mutex lock
    print 'Thread %s done after %s seconds' %(myId, count)
    m.release() # releases the mutex lock
    childStatus[myId] = 1 # changes the position in the list from 0 -> 1 for the thread that it's on.



# START OF PROGRAM
raw_input("Press 'Enter' to start")
nT = util.getInt('How many threads would you like to start: ', 'Unable to use that value, so try again')
childStatus = [0] * nT # creates a list of 0's based off user input ex: nt = 3 childStatus = [0, 0, 0]
m = thread.allocate_lock() #starts the mutex lock
for i in range(nT):
	thread.start_new(counter, (i, random.randint(1,20)))

# Checks to end script
while 0 in childStatus: 
	pass 
print 'Nothing to see here; move along now.\nKeegan Bailey made this.' 
