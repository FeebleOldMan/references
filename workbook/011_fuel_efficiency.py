MPG_TO_L100KM = 235.215

mpg = float(input("Enter fuel efficiency (MPG): "))
print("Fuel efficiency: {:.2f} L/100km".format(mpg*MPG_TO_L100KM))
