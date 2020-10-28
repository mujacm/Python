#Python Program to take input for Matrix formation

M = []

#input for no. of rows and no. of columns
r = int(input("Enter no. of rows: "))
c = int(input("Enter no. of columns: "))


for i in range(r):
    l1 = []
    for j in range(c):
        t = int(input("Enter a value: "))
        l1.append(t)
    M.append(l1)

#Formation of a matrix
for i in range(r):
    for j in range(c):
        print(M[i][j], end = "\t")
    print()
