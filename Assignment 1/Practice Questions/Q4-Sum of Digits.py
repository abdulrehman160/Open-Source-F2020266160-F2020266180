#--Question 4: Sum of Digits
def sum_of_digit(n):
  n=abs(n) #--if number is negative then convert absolute value
  sum=0
  while n!=0: #--loop to add the digits
   digit=n%10 #--extract the last digit
   sum+=digit
   n=n//10 #--remove the last digit

  return sum #--return the sum of digits

num=int(input("Enter the Number: "))
print(sum_of_digit(num)) 