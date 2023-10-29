#--Question 9:  Count Vowels and Consonants
import re
def count_vowels_consonants(str):
  str = str.replace(" ", "").lower() #--remove spaces and convert the upper cases into lower cases
  str=re.sub(r'\d','',str) #--remove numbes from string
  new_list=list(str) #--convert string into list Because the string is immutable in python

  vowels_count=0 
  consonants_count=0

  itrater=0
  while itrater!=len(new_list):
    alphabet=new_list[itrater]
    if alphabet=='a' or alphabet=='e' or alphabet=='i' or alphabet=='o' or alphabet=='u':
      vowels_count+=1
    else:
      consonants_count+=1

    itrater+=1

  print("Total Vowels in string: ",vowels_count)
  print("Total Consonants in string: ",consonants_count)

str=input("Enter the string: ")
count_vowels_consonants(str)