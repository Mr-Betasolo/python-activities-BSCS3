year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 != 0:
        isLeapYear = True
    elif year % 100 == 0 and year % 400 == 0:
        isLeapYear = True
    else:
        isLeapYear = False

if isLeapYear:
    print(str(year) + " is a Leap Year.")
else:
    print(str(year) + " is not a Leap Year.")