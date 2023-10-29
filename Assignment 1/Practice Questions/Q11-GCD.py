#--Question 11: Find GCD  (Greatest Common Divisor)
def get_gcd(num1, num2):
    #--change negative value to positive value
    num1=abs(num1)
    num2=abs(num2)
    #--Edge cases
    if num1 == 0: #--if any of the number is 0 then return the other number 
        return num2
    if num2 == 0:
        return num1

    while num1 != num2: #--loop to find the gcd
        if num1 > num2: #--if num1 is greater than num2 then subtract num2 from num1
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return num1 

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
gcd = get_gcd(num1, num2)

print("The Greatest Common Divisor is:", gcd)