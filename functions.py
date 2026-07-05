def greeting(*numbers):
    
    print("Hi! Welcome back")
    sum = 0
    for i in range(0,len(numbers)):
        sum = sum + numbers[i]

    return sum



sums = greeting(12,1,3)
print(sums)