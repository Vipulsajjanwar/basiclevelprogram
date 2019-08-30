print("Program to print start pattern: \n");
rows = input("Enter max star to be display on single line")
rows = int (rows)
for i in range (1, rows):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\r")
for i in range (rows, 1, -1):
    for j in range(1, i -1):
        print(j, end=' ')
    print("\r")