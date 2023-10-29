#--Question 12: find LCM(Least Common Multiple)
#--Formula of LCM: LCM(a,b) * GCD(a,b)= a * b
#--So the LCM IS: LCM(a,b) = a * b/GCD(a,b)
#--First of all find the GCD(a,b) and then put in above formula
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

#--Function for LCM(a,b)
def get_lcm(num1,num2): 
  lcm=abs(num1*num2)//get_gcd(num1,num2) #--GCD(a,b) put in formula of LCM(a,b)
  return lcm


num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
lcm=get_lcm(num1,num2)
print("The Least Common Multiple is: ",lcm)