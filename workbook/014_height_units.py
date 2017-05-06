FT_TO_IN = 12
IN_TO_CM = 2.54

feet = float(input("Enter height (ft): "))
inch = float(input("Enter height (in): "))

print("Height (cm): {}".format((feet*FT_TO_IN+inch)*IN_TO_CM))
