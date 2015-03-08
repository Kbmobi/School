import thread, time

def counter(myId, count, m):
  for i in range (count):
    time.sleep(1)
    m.aquire()
    print 'Thread %s at count %s' % (myId, i)
    m.release()

m = thread.allocate_lock()    
for i in range(10):
  thread.start_new(counter, (i, 5, m))

time.sleep(30)
print 'Main thread done'
