#--Question 3: Generate Fibonacci Sequence
def fibonacci_series(n):
  if n==0 or n==1:#--Edge case 
    print(n)
    return
  a=0
  b=1
  print(a, end=" ")
  print(b, end=" ") #--print the first two numbers
  for i in range(2,n+1): #--loop to print the rest of the numbers
    temp=a+b #--temporary variable to store the sum of the previous two numbers
    a=b
    b=temp
    print(b, end=" ")

num=int(input("Enter the Number: "))
fibonacci_series(num)
