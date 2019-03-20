#Question:
#  Reverse the provided string. You may need to turn the string into an array before you can reverse it. Your result must be a string.

# prompting user to input the string

input_string = (input("Type any word: "))

# to reverse a string using the extended slicing approach
# according to the syntax str[start:end:step] . the start is by default 0 in both the cases. in first case the string is printed from index value 0.

def reverse_string(str):
   
    str_reverse = input_string[::-1]

    print(str_reverse)

reverse_string(input_string)