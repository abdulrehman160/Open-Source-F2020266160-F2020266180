# library to use system max and min size 
import sys
def is_maximum_minimum(my_list):
  if len(my_list)==1:
    print("The maximum number is: ", my_list[0])
    print("The minimum number is: ", my_list[0])
    return
  max=-sys.maxsize-1
  min=sys.maxsize

  itrater=0
  while itrater<len(my_list):
    element=int(my_list[itrater])
    if element>max:
      max=element
    if element<min:
      min=element
    itrater+=1

  print("The maximum number is: ", max)
  print("The minimum number is: ", min)

user_input = input("Enter a list of items separated by commas: ")
user_list = user_input.split(',')
is_maximum_minimum(user_list)