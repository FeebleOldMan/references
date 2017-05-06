while True:
    human_years = float(input("Enter human years: "))
    if human_years >= 0:
        break
    else:
        print("ERROR: Enter a positive number")

if human_years >= 2:
    dog_years = 2 * 10.5 + (human_years-2) * 4


print("Dog years: {}".format(dog_years))
