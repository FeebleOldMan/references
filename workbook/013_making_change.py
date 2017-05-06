COIN_VALUES = {
    "1 dollar": 100,
    "50 cents": 50,
    "20 cents": 20,
    "10 cents": 10,
    " 5 cents": 5,
    " 1 cent ": 1
    }

total = int(input("Cash (cents): "))

for coin, value in COIN_VALUES.items():
    print("{}: {}".format(coin, total//value))
    total %= value
