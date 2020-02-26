def compute_lcm (a,b):
    if a>b :
        greater = a
    else :
        greater = b
    while 1 :
        if ( greater % a == 0 and greater % b == 0 ):
            lcm = greater
            break
        greater = greater+1
    return lcm

a = int(input("Enter num1 : "))
b = int(input("Enter num2 : "))
print ("The L.C.M :  ", compute_lcm (a,b))
