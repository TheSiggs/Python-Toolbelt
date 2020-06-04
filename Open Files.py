# The Bad Way (But will print everything nicely)
f = open('text.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()

# The better Way (But wont print everything nicely)
f = open('text.txt')
for line in f:
    print(line)
f.close()

# The even better Way (But wont print everything nicely)
with open('text.txt') as f:
    for line in f:
        print(line)

# Uses a generator, Even better way (But wont print everything nicely)
def readfile(path, delim):
    return (ln.split(delim) for ln in open(path, 'r'))