def greeting():
    numlist = []
    print("Hi! Welcome back")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    numlist.append(num1)
    numlist.append(num2)

    return num1, num2

numbers = greeting()
print(numbers)