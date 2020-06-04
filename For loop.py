needle = 'd'
haystack = ['a', 'b', 'c']

#  The good way to search for an element within a list
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else:  # If no break is found
    print('Not Found!')
