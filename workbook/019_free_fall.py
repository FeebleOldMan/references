GRAVITATIONAL_ACCELERATION = 9.8
height = float(input("Height (m): "))
print("Final velocity in free fall (m/s): {}".format(
    (2*GRAVITATIONAL_ACCELERATION*height)**0.5
    )
    )
