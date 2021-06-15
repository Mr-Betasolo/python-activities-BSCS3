import random

randomNum1 = random.randint(0, 10)
randomNum2 = random.randint(0,10)
print("First Number: " + str(randomNum1))
print("Second Number: " + str(randomNum2))

print("\n====Operation====\nA: Addition\nB: Subtraction\nC: Multiplication\nD: Division")
operation = input("\nChoose Operation: ")


if operation in ['a', 'A', 'Addition', 'ADDITION', 'addition', 'add', '+', 'sum']:
    correctAns = randomNum1 + randomNum2
    userAns = int(input("\nWhat is the sum? "))
    if correctAns == userAns:
        print("Correct")
    else:
        print("Wrong! The correct answer is " + str(correctAns))
elif operation in ['b', 'B', 'Subtraction', 'SUBTRACTION', 'subtraction', 'subtract', '-', 'difference']:
    correctAns = randomNum1 - randomNum2
    userAns = int(input("\nWhat is the difference? "))
    if correctAns == userAns:
        print("Correct")
    else:
        print("Wrong! The correct answer is " + str(correctAns))
elif operation in ['c', 'C', 'Multiplication', 'MULTIPLICATION', 'multiplication', 'multiply', '*', 'product']:
    correctAns = randomNum1 * randomNum2
    userAns = int(input("\nWhat is the product? "))
    if correctAns == userAns:
        print("Correct")
    else:
        print("Wrong! The correct answer is " + str(correctAns))
elif operation in ['d', 'D', 'Division', 'DIVISION', 'division', 'divide', '/', 'quotient']:
    correctAns = randomNum1 / randomNum2
    userAns = float(input("\nWhat is the quotient? "))
    if correctAns == userAns:
        print("Correct")
    else:
        print("Wrong! The correct answer is " + str(correctAns))
else:
    print("\nError: Invalid Operation")


