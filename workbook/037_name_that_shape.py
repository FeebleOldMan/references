SHAPES = {
    3: "Triangle",
    4: "Square",
    5: "Pentagon",
    6: "Hexagon",
    7: "Septagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon",
    }

sides = int(input("Enter number of sides: "))
try:
    print(SHAPES[sides])
except KeyError:
    print("Shape not in database.")
