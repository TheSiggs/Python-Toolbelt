income = [10, 30, 75]
# I want to double me money


# one way to do it
def double_money(dollars):
    return dollars * 2

# Another way of doing it
new_income = list(map(double_money, income))
print(new_income)