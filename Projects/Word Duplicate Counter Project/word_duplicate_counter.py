"""
This is a simple project that uses dictionaries to store words (key) and frequencies (values)
The program reads text thats received from the user's input and counts the frequencies of each word
After counting the words, it will print out the words and their frequencies
"""
# word_frequencies ={} # empty dictionary
# user_text = input("Enter in some text to see how many repeated words there are:")
# word_count = 0

# split_words=user_text.split()  # split each word from the user's input and put it in a list
# for every_word in split_words:  # go through every word in the list to see if there are any repeated words 
#     count_words = every_word.count("some") # fix this tmrw
#     print(count_words)
#     if every_word != 1: # this conditional statement sees if the word repeats or doesn't repeat.The problem is here since the word count will always be one
#         word_count+=1
#     else:
#         word_count=1
#     repeated_words=dict({every_word:count_words})
#     word_frequencies.update(repeated_words)
# print(word_frequencies)



# Rewriting everything to see if the problem can be solved

user_text={}   # empty dictionary
user_input=input("Enter some text to see if there are any repeated words:")   # ask the user for their input
user_input_split_text=user_input.split()
word_count={}
duplicate_words=[]

for every_word in user_input_split_text:
    word_count[every_word] = word_count.get(every_word,0)+1  
    if word_count[every_word] >1 and every_word not in duplicate_words:  # check if a word's count is above one and not in the duplicate_words list
        duplicate_words.append(every_word)  # add any duplicated words
    
    """
    word_count[every_word] goes through each word and assigns itself that word. On the right side, thats where the dictionary gets each letter and adds 1 to every letter since they appear in the user's text.
    word_count[every_word] = word_count.get(every_word,0)+1
    -> word_count["Bob"]={"Bob",1}
     This line of code was from ChatGPT 3.5. I've learned a lot after looking and trying this code out after explaining how it works.
    """
if duplicate_words:
    print("\nHere are the duplicated word(s): {}".format(duplicate_words))
else:
    print("No duplicate words")
    
print("\nHere is the list of words: {}\n".format(word_count))