
def reverse_string(str):
  
  #converting the string into list cause string is not change able  in python
  str_list=list(str)

  #Two pointers Approach
  start=0
  end=len(str_list)-1

  while start<=end:
    temp=str_list[start]
    str_list[start]=str_list[end]
    str_list[end]=temp

    start+=1
    end-=1
  
  #join function for convert the list into string
  reversed_str=''.join(str_list)
  print(reversed_str)

str=input("Enter the string: ")
reverse_string(str)