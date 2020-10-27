def bubblesort(a):
   n = len(a)
   
   for i in range(n):
   
       for j in range(0, n-i-1):
     
           if a[j] > a[j+1] :
               a[j], a[j+1] = a[j+1], a[j]

a = ['t','u','t','o','r','i','a','l']
bubblesort(a)
print ("Sorted array is:")
for i in range(len(a)):
   print (a[i])