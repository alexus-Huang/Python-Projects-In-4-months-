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