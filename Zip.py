first = ['Buckey', 'Sam', 'Taylor']
last = ['Roberts', 'Siggs', 'Swift']

# Two ways to combine two lists
names = zip(first, last)
for a, b in names:
    print(a, b)


for x, y in zip(first, last):
    print(x, y)
