def number_to_word(words_list , num):
  num=abs(num) #--change negative value to positive value

  if num==0:
    print("Number in words: Zero")
    return

  ans_list=[]
  while num!=0:
    # get last digit from no
    digit=num % 10

    # remove last digit from no
    num=num // 10

    # add the word at first index
    ans_list.insert(0,words_list[digit-1])

  # convert the list into string with spaces with join()
  print("Number in words:", " ".join(ans_list)) 

words_list=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
num=int(input("Enter the number: "))
number_to_word(words_list,num)