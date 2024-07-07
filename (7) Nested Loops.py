# nested loops: The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("What symbol?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol + " ", end="") # as the symbol will be print to the next line, we'll use (end="") so that once the entered no. of columns are printed, it'll move on to the next line
    print()


for i in range(rows):
    for i in range(columns):
        print(symbol, end="")
    print()