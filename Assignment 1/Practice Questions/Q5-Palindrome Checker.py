#--Question 5: check palindrome
def is_palindrome(str):
  str = str.replace(" ", "").lower() #--Remove the spaces and convert upper case to lower case
  if len(str)==1: #--Edge case
    print("Yes Palindrome")
    return
#--Two pointers Approach
  start=0
  end=len(str)-1

  while start<=end: #--loop to check the palindrome
    if str[start]!=str[end]: #--if the characters are not equal then it is not a palindrome
      print("Not Palindrome.")
      return
    start+=1
    end-=1

  print("Yes Palindrome.") #--if the loop is completed then it is a palindrome

str=(input("Enter the string: "))
is_palindrome(str)  