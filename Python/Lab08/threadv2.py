#! /usr/bin/python

import thread, time, random, util

def counter(myId, count):
    global childStatus
    time.sleep(count)
    m.acquire()
    print 'Thread %s done after %s seconds' %(myId, count)
    m.release()
    childStatus[myId] = 1
	
raw_input("Press 'Enter' to start")
nT = util.getInt('How many threads would you like to start', 'Unable to use that value, so try again')
childStatus = [0] * nT
m = thread.allocate_lock()
random.seed()
for i in range(nT):
	thread.start_new(counter, (i, random.randint(1,20)))

while 0 in childStatus:
	pass 
print 'Main thread done'
