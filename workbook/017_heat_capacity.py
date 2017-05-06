HEAT_CAPACITY = 4.186
J_TO_KWH = 1/3600000
COST_PER_KWH = 0.089

mass = float(input("Mass (g): "))
delta_temp = float(input("ΔT (°C): "))
joules = mass*HEAT_CAPACITY*delta_temp
cost = joules*J_TO_KWH*COST_PER_KWH
print("Energy required (J): {}".format(joules))
print("Cost of electricity ($): {}".format(cost))
