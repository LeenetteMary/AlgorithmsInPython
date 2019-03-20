# Returning the length of the longest word in the provided sentence. 

# user input sentence
sentence = input("Enter your preferred sentence: ")

def find_longest_word(sentence):  
    longest_word = ''       # initial value of the longest word
    for word in sentence:
        if len(word) > len(longest_word): # comparing words in sentence
        # finding the longest of them all using the max() function
            longest_word = max(sentence, key=len)    
          
            print(longest_word, len(longest_word))  # outputing the result
 
word_list = sentence.split()  # seperating the words in sentence
find_longest_word(word_list)  

 