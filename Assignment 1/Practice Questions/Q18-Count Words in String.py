def count_words(input_string):

    # Split the input string into words using whitespace as the delimiter
    words = input_string.split()

    # Count the number of words
    number_of_words = len(words)
    return number_of_words


str=input("Enter the string: ")                
number_of_words = count_words(str)
print("Number of words in the string:", number_of_words)