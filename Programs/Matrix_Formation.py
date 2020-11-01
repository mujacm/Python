#Program for Matrix Formation
M = []

#Taking Input from user 
#for no. of rows and columns
r = int(input("Enter no. of rows: "))
c = int(input("Enter no. of columns: "))


#Taking Values as input for Matrix
for i in range(r):
    l1 = []
    for j in range(c):
        t = int(input("Enter a value: "))
        l1.append(t)
    M.append(l1)

for i in range(r):
    for j in range(c):
        print(M[i][j], end = "\t")
    print()
