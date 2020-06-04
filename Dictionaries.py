ages = {
    'Mary': 31,
    'John': 28,
    'Dick': 51
}
# Pulling specific elements from dictionaries and display them in a string
print('# The bad way')
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old' % age)

# Use the .get() function for this!!
print()
print('# The good way')
age = ages.get('Dick', 'Unknown')
print('Dick is %s years old' % age)

# --------------------
# Sorting Dictionaires
# --------------------
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print('min', max(zip(stocks.values(), stocks.keys())))
print('max', min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))