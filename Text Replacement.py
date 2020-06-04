import sys

count = 0
while True:
    count += 1
    sys.stdout.write('Counting: %s\r' % count)
    sys.stdout.flush()
