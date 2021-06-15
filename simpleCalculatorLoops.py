import random

correct = 0
wrong = 0


def generatefirstnumber():
    num1 = random.randint(1, 10)
    return num1


def generatesecondnumber():
    num2 = random.randint(1, 10)
    return num2


while True:
    randomNum1 = generatefirstnumber()
    randomNum2 = generatesecondnumber()

    print("First Number: " + str(randomNum1))
    print("Second Number: " + str(randomNum2))

    print("\n====Operation====\nA: Addition\nB: Subtraction\nC: Multiplication\nD: Division")
    operation = input("\nChoose Operation: ")

    if operation in ['a', 'A', 'Addition', 'ADDITION', 'addition', 'add', '+', 'sum']:
        correctAns = randomNum1 + randomNum2
        userAns = int(input("\nWhat is the sum? "))
    elif operation in ['b', 'B', 'Subtraction', 'SUBTRACTION', 'subtraction', 'subtract', '-', 'difference']:
        correctAns = randomNum1 - randomNum2
        userAns = int(input("\nWhat is the difference? "))
    elif operation in ['c', 'C', 'Multiplication', 'MULTIPLICATION', 'multiplication', 'multiply', '*', 'product']:
        correctAns = randomNum1 * randomNum2
        userAns = int(input("\nWhat is the product? "))
    elif operation in ['d', 'D', 'Division', 'DIVISION', 'division', 'divide', '/', 'quotient']:
        correctAns = randomNum1 / randomNum2
        userAns = float(input("\nWhat is the quotient? "))
    else:
        print("\nError: Invalid Operation")
        break

    if correctAns == userAns:
        print("Correct")
        correct += 1
    else:
        print("Wrong! The correct answer is " + str(correctAns))
        wrong += 1

    print("\n====POINTS====")
    print("Correct: " + str(correct))
    print("Wrong: " + str(wrong))

    question = input("\nDo you still want to continue? Yes (Y) or No (N): ")
    if question in ['Y', 'y', 'YES', 'yes', 'Yes']:
        pass
    elif question in ['N', 'n', 'NO', 'no', 'No']:
        print("\nThank you for playing!")
        break

    print('==============================================================\n')

