#sum

print("Enter 2 numbers")
a = int (input())
b = int( input ())

print ("values of entered numbers are : "+ str(a)  +"|" + str(b))

t=a
a=b
b=t

print("after swap the values are : "+ str(a) +"|" + str(b))