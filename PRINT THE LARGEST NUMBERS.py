a = float(input("Enter the first number : "))
b = float(input ("Enter the Second Number : "))
c = float(input("Enter the Third Number :"))
if (a>b) and (a>c):
    print("largest Number : ",a)
elif (b>c):
    print("largest Number : ",b)
else:
    print("largest Number : ",c)