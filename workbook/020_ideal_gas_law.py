IDEAL_GAS_CONSTANT = 8.314
C_TO_K = 372.15

pressure = float(input("Pressure (Pa): "))
volume = float(input("Volume (L): "))
temperature = float(input("Temperature (C): "))
print("Amount (Mol): {}".format(
    (pressure*volume)/(IDEAL_GAS_CONSTANT*(temperature+C_TO_K))
    ))
