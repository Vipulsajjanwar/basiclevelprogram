
if __name__ == '__main__':

    a, b, i, j, flag = 0, 0, 0, 0, 0

    a = 1
    print(a)

    print("Enter Nth term:",end="")
    b = int(input())
    print(b)

    # Print display message
    print("Prime numbers between", a, "and",
          b, "are:", end="")


    for i in range(a, b + 1):

       if (i == 1):
            continue
            flag = 1

    for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break

                if (flag == 1):
                    print(i, end=" ")


