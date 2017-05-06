s1 = float(input("Length of side 1: "))
s2 = float(input("Length of side 2: "))
s3 = float(input("Length of side 3: "))
s = (s1 + s2 + s3) / 2
area = (s * (s - s1) * (s - s2) * (s - s3))**0.5
print("Area of triangle: {}".format(area))
