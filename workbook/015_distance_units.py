DISTANCES = {
    'Distance (in)': 12,
    'Distance (yd)': 0.333333,
    'Distance (mi)': 0.000189394,
    }
feet = float(input("Distance (ft): "))

for distance, value in DISTANCES.items():
    print('{}: {}'.format(distance, feet*value))
