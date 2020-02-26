year = int(input("Enter a year :"))
if ( year%4 == 0) and (year % 400 == 0) and (year % 400 == 0   ):
    print(year,"is a leap year" )
else :
    print("{0} is a leap year".format(year))
