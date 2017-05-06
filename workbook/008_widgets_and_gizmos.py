WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112
widget_count = int(input("Number of widgets: "))
gizmo_count = int(input("Number of gizmos:: "))
print("Total weight (g): {}".format(
    widget_count*WIDGET_WEIGHT
    + gizmo_count*GIZMO_WEIGHT
    ))
