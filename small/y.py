## Print the required output in given format
n = int(input())
for i in range(1, n+1):
    for j in range(i, 0):
        print(j, end="")
    print()