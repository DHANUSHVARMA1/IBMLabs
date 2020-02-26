import cmath
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))
d = (b ** 2)-(4 * a * c)
sol1 = (-b - cmath.sqrt(d) / (2*a))
sol2 = (-b + cmath.sqrt(d) / (2*c ))
print("The solution is : {0} and {1} ".format(sol1,sol2))
