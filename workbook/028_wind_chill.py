T = 100
V = 0
while T > 10:
    T = float(input("Air temperature (C): "))
    if T > 10:
        print("Please enter a temperature <= 10C")
while V <= 4.8:
    V = float(input("Wind speed (km/h): "))
    if V <= 4.8:
        print("Please enter a wind speed > 4.8 km/h")
print("Wind Chill Index (C): {}".format(
    int(round(13.12 + 0.6215*T - 11.37*(V**0.16) + 0.3965*T*(V**0.16)))
    )
    )
