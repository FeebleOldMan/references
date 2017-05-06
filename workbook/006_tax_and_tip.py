GST = 0.07
SERVICE = 0.1
cost_of_meal = float(input("Cost of meal: "))
print("Service Charge: ${:.2f}".format(SERVICE*cost_of_meal))
print("GST: ${:.2f}".format(GST*(1+SERVICE)*cost_of_meal))
print("TOTAL: ${:.2f}".format((1+GST)*(1+SERVICE)*cost_of_meal))
