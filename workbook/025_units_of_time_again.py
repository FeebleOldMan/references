TIME_CONVERSIONS = {
    'D': 86400,
    'HH': 3600,
    'MM': 60,
    'S': 1
    }

seconds = int(input("Time (s): "))
for key, value in TIME_CONVERSIONS.items():
    if key == 'D':
        print('{:01}'.format(seconds//value), end="")
    else:
        print(':{:02}'.format(seconds//value), end="")
    seconds %= value
print()
