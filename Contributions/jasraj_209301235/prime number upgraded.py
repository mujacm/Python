#progaram to list all prime numbers within a given range which is provided by the user

start = int(input("Enter beginning of range :"))
finish = int(input("Enter ending of range :"))

print("Prime numbers between", start, "and", finish, "are:")

for num in range(start, finish + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)