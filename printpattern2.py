x=int(input("enter the last no:"))
print("Second Number Pattern ")
lastNumber = x
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")