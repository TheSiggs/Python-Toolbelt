# Factorial recursion
def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)


def explode(word):  # Expand word
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])


def removeDupes(word):  # Remove duplicates
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDupes(word[1:])
    else:
        return word[0] + removeDupes(word[1:])


def sumTheList(List, size):
    if size == 0:
        return 0
    else:
        return List[size - 1] + sumTheList(List, size - 1)
