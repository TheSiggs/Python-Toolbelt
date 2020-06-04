import sys
import time

count = 0
while True:
    time.sleep(1)
    count += 1
    sys.stdout.write('%s\r' % count)
    sys.stdout.flush()
