height = float(input("Height (cm): "))/100
weight = float(input("Weight (kg): "))
BMI = weight / height**2
print("BMI: {:.2f}".format(BMI))
