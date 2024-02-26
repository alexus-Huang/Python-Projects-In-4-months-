"""
This is a simple project that uses dictionaries to store words (key) and frequencies (values)
The program reads text thats received from the user's input and counts the frequencies of each word
After counting the words, it will print out the words and their frequencies
"""
word_frequencies ={} # empty dictionary
user_text = input("Enter in some text to see how many repeated words there are:")
word_count = 0

split_words=user_text.split()  # split each word from the user's input and put it in a list
for every_word in split_words:  # go through every word in the list to see if there are any repeated words 
    count_words = every_word.count(every_word)
    if every_word != 1: # this conditional statement sees if the word repeats or doesn't repeat.The problem is here since the word count will always be one
        word_count+=1
    else:
        word_count=1
    repeated_words=dict({every_word:count_words})
    word_frequencies.update(repeated_words)
print(word_frequencies)
