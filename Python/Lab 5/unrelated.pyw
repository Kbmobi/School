#2 (the program that receives the variable and counts up)
def countup(base, x):         # recursive
    if x <= 998:
        base += 1
        x += 1
        print base
        return countup(base, x)
    print "poop"

if __name__ == "__main__":
    start = input ('want me to count: ')
    stop = 1
    countup(start, stop)
