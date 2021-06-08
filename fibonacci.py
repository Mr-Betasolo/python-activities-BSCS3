interval = int(input("Enter a number: "))

fib1 = 0
fib2 = 1
temp = 0
fibString = ""

for i in range(interval):
    fibString += str(fib1) + " "
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp

print("\nFibonacci Sequence:\n" + fibString)
