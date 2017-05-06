from math import pi, tan

s = int(input("Length of sides: "))
n = int(input("Number of sides: "))
area = (n * s**2) / (4 * tan(pi/n))
print("Area of regular polygon: {}".format(area))
