"""
This is a simple project that uses dictionaries to store words (key) and frequencies (values)
The program reads text thats received from the user's input and counts the frequencies of each word
After counting the words, it will print out the words and their frequencies
"""
word_frequencies ={} # empty dictionary
user_text = input("Enter in some text to see how many repeated words there are:")
word_count = 0

split_words=user_text.split()  # split each word from the user's input and put it in a list
for every_word in split_words:
    print(every_word.count(every_word))
    repeated_words=dict({every_word:word_count})
    print(repeated_words)
