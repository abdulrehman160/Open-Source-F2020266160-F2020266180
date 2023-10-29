#--Question 1: calculate factorial 
#--With loop
def get_factorial(n):
  if n==0 or n==1:#--Edge case
    return 1
  ans=1
  for i in range(1,n+1):
    ans=ans*i
  return ans

num=int(input("Enter the number: "))#--user input
print(get_factorial(num))#--print the factorial of the number