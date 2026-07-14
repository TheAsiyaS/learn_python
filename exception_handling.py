num = input("Enter a number: ")

try:
    num = int(num)
    print("number is int:", num)
except ValueError:
    print("Enter a value other than a int")