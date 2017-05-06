number = [int(n) for n in input("Enter an integer: ")]
print(*number, sep="+", end="="+str(sum(number))+"\n")
