name = input("Name: ")
prelim = float(input("\n1st Quarter: "))
midterm = float(input("2nd Quarter: "))
semis = float(input("3rd Quarter: "))
final = float(input("4th Quarter: "))

average = (prelim + midterm + semis + final) / 4
print("\nAverage: " + str(average))

if (average >= 98 and average <=100):
    print("Remarks: With Highest Honors")
elif average >= 95:
    print("Remarks: With High Honors")
elif average >= 90:
    print("Remarks: With Honors")
elif average >= 75:
    print("Remarks: Passed")
elif average >= 51:
    print("Remarks: Failed")
else:
    print("Error: Invalid Grade")