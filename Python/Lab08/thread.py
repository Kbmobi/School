#! /usr/bin/python

import thread, time, util, random

#def wait():
 #   time.sleep(random.randint(1, 20))

def count(myId, count, m):
    for i in range(count):
        time.sleep(0.1)
        m.acquire()
        print 'Thread %s at count %s at %s seconds' % (myId, i) 
        m.release()
        
def stNew(n, m):
    for i in range(n):
        thread.start_new(count, (i, 5, m))


m = thread.allocate_lock()
threadCount = util.getInt('Please input the number for the range of threads: ', 'error')
stNew(threadCount, m)
