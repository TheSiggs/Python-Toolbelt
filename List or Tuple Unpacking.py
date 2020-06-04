# Make sure the number of varibles equals the number of items in the list!!
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
# print(date)
# print(name)
# print(price)


def drop_first_and_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_and_last([65, 76, 98, 54, 21, 23, 45, 99])
