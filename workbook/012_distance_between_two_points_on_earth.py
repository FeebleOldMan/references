from math import acos, cos, sin, radians
EARTH_RADIUS = 6371.01
t1, g1 = map(
    radians, map(
        float, input("Point 1 (lat, lon): ").strip().split(",")
        )
    )
t2, g2 = map(
    radians, map(
        float, input("Point 2 (lat, lon): ").strip().split(",")
        )
    )

print("Distance: {:.2f} km".format(
    EARTH_RADIUS * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
    )
     )
