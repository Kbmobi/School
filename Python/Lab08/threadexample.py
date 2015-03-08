# Thread example.

# Modified from an example in Programming Python, Mark Lutz, O'Reilly
# by Deid Reimer 2003-10-20  reimer@camosun.bc.ca

# Load the thread and time libraries
import thread, time

# Create the thread function
def counter(myId, count):
  for i in range (count):
    time.sleep(1)
    print 'Thread %s at count %s' % (myId, i)

# Main program.  Starts 10 threads.  Each thread counts from 0 to 4.
# It then sleeps for 30 seconds to ensure all the threads have completed.
# If the parent thread exits before the children are finished, the children
# will be killed as well.
for i in range(10):
  thread.start_new(counter, (i, 5))

time.sleep(30)
print 'Main thread done'