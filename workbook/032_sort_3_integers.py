numbers = list(map(int, input("Enter 3 integers: ").strip().split()))
print("Sorted: ", end="")
print(*sorted(numbers), sep=" ")
