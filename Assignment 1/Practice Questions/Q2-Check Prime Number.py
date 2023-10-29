
userInput = int(input("Enter a No to check is a prime or not: "))

if userInput == 2:
    userInput += 1
    userInput % 2 == 1
    print('Number is a Prime Number')
elif userInput % 2 == 1:
    print('Number is a Prime Number')
else:
    print("Number is not a Prime Number!!!") 



