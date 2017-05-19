MONTH_WORD_TO_NUM = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12,
    }

month = input("Enter the month: ")[:3]

# check if input is string to convert to int
try:
    month = month[:3].lower()
    month = MONTH_WORD_TO_NUM[month]
except KeyError:
    pass

try:
    month = int(month)
except ValueError:
    raise ValueError("Error in input")

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("28 or 29 days")
