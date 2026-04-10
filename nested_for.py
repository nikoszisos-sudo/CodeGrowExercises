rows = int(input("Input a number of rows: "))
columns = int(input("Input a number of columns: "))
symbol = input("Input a symbol: ")
for row in range(rows):
    for column in range(columns):
        print(f"{symbol} ", end=" ")
    print()
