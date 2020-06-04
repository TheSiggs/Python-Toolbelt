print('Converting')
try:  # Try this!
    print(int('1'))
except:  # If it doesn't work
    print('Conversion failed')
else:  # if it did work
    print('Coversion sucessful!')
finally:  # Always do this
    print('Done!')

# With "finally", if we try and an error occus, before the program crashes
# everything in the finally bock will be run and then the program will crash

# Below will work!
# try:
# finally:
