SMALL_DEPOSIT = 0.1
LARGE_DEPOSIT = 0.25

small_bottles = int(input("Number of bottles <= 1L: "))
large_bottles = int(input("Number of bottles >  1L: "))
refund = small_bottles*SMALL_DEPOSIT + large_bottles*LARGE_DEPOSIT
print("Refund: ${:.2f}".format(refund))
