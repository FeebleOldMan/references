INTEREST = 0.04
YEARS = 3
deposit = float(input("Deposit: $"))
for i in range(1, YEARS+1):
    deposit *= 1+INTEREST
    print("Year {}: ${:.2f}".format(i, deposit))
