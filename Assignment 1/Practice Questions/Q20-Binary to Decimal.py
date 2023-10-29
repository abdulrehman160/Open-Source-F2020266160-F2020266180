def binary_to_decimal(binary_number):
  decimal=0
  i=0
  while binary_number!=0:
   
   # get last digit from binary
   digit=binary_number % 10

   # remove last digit from binary
   binary_number=binary_number // 10

   # check if the digit is 1(odd)
   if digit & 1:
    decimal+=2**i
   i+=1

  print("The Decimal of given Binary: ",decimal)

num=int(input("Enter the number: "))
binary_to_decimal(num)