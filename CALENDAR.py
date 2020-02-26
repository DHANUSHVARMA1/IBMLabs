import calendar
yy = int(input("Enter year : "))
mm = int(input("Enter month :"))
day = int(input("Enter day : "))
print(calendar.month(yy,mm))
print(calendar.calendar(yy))
print("Leap year : ",calendar.isleap(yy))
print(calendar.weekday(yy,mm,day))

