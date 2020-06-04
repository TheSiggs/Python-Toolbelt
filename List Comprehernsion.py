nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('''#---------
# Example 1
# ---------
# I want 'n' for each 'n' in nums''')
# FOR LOOP
print('FOR LOOP')
myList = []
for n in nums:
    myList.append(n)
print(myList)

# LIST COMP
print('LIST COMP')
myList = [n for n in nums if n > 5]
print(myList)

print('''#---------
# Example 2
# ---------
# I want 'n*n' for each 'n' in nums''')
# FOR LOOP
print('FOR LOOP')
myList = []
for n in nums:
    myList.append(n * n)
print(myList)

# LIST COMP
print('LIST COMP')
myList = [n * n for n in nums]
print(myList)

# using map + lambda
print('OTHER METHOD')
myList = map(lambda n: n * n, nums)
print(myList)

print('''#---------
# Example 3
# ---------
# I want 'n' for each 'n' in nums if 'n' is even''')
# FOR LOOP
print('FOR LOOP')
myList = []
for n in nums:
    if n % 2 == 0:
        myList.append(n)
print(myList)

# LIST COMP
print('LIST COMP')
myList = [n for n in nums if n % 2 == 0]
print(myList)

# Filter and lambda functions
print('OTHER METHOD')
myList = filter(lambda n: n % 2 == 0, nums)
print(myList)
print('''#---------
# Example 4
# ---------
# I want a letter number pair in "abcd" and each number in "0123"''')
# FOR LOOP
print('FOR LOOP')
myList = []
for letter in 'abcd':
    for num in range(4):
        myList.append((letter, num))
print(myList)

# LIST COMP
print('LIST COMP')
myList = [(letter, num) for letter in 'abcd' for num in range(4)]
print(myList)

print('''#---------
# Example 5
# ---------''')
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# FOR LOOP
print('FOR LOOP')
myDict = {}
for name, hero in zip(names, heros):
    myDict[name] = hero
print(myDict)

# LIST COMP
print('LIST COMP')
# myDict = {name: hero for name, hero in zip(
#     names, heros) if name != 'Peter'}  # Removed a Peter
myDict = {name: hero for name, hero in zip(names, heros)}  # Prints full list
print(myDict)

print('''#---------
# Example 6
#---------''')
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# FOR LOOP
print('FOR LOOP')
mySet = set()
for n in nums:
    mySet.add(n)
print(mySet)

# LIST COMP
print('LIST COMP')
mySet = {n for n in nums}
print(mySet)

print('''#---------
# Example 7
#---------
# Generator Expression
# I want to yeild 'n*n' for each 'n' in nums''')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# FOR LOOP
print('FOR LOOP')


def genFunc(nums):
    for n in nums:
        yield n * n

myGen = genFunc(nums)

for i in myGen:
    print(i)

# LIST COMP
print('LIST COMP')
myGen = (n for n in nums)
for i in myGen:
    print(i)
