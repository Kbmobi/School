#

#
# Binary search function
# Parameters: book - a list of names
#             name - a name to search for
# Returns:    position in list at which name was found,
#             or None if not found

def search (book, name):
    left = 0                            # beginning of list
    right = len (book) - 1              # end
    found = 'no'                        # not found yet
    while left <= right and found == 'no':
        mid = (left + right) / 2        # midpoint (round down)
        if name == book[mid]:           # found it!
            found = 'yes'
            position = mid
        elif name < book[mid]:          # Go left young man
            right = mid - 1
        else:                           # Go right
            left = mid + 1

    if found == 'yes':                  # Why did we stop looping
        return position                 # found the entry
    else:
        return None                     # It's not there


#
# Test code
# Read in a list of names (must be sorted)
# and the search name
# call search function and report back
#

if __name__ == '__main__':
    Book = input ('Enter names: ')
    Name = raw_input ('Enter name to search for: ')

    while Name != '':
        position = search (Book, Name)
        if position == None:
            print Name, 'not found'
        else:
            print Name, 'found at', position
        Name = raw_input ('Enter name to search for: ')
