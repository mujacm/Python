# Program to check string is palindrome or not

while True:        
    
    str1 = "racecar"

    # To take input from the user
    # str1 = input("Enter a string: ")

    # defining an empty string
    str2 = ""

    #defining length of str1
    n = len(str1)

    for i in range(-1,-n-1,-1):
        pos = str1[i]
        str2 = str2 + pos
    print(str2)
    print()

    #if str1 is equal to str2
    #then string is palindrome
    if str2 == str1:
        print("Entered string is a palindrome")
    else:
        print("It is not a palindrome")
