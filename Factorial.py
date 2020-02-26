a = int(input("Enter a Number : "))
factorial = 1
if a<0 :
    print("Factorial is not possible for negative numbers.")
elif a == 0 :
    print("The factorial is : 1")
else :
    for i in range(1,a+1):
        factorial = factorial*i
    print("The factorial of ",a,"is",factorial)