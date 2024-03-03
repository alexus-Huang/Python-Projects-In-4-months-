"""
This game uses:
    Lists - keeps a list of words
    Loops - to either keep the game running or stop the game
    A dictionary - stores player scores

The word changes every time the game restarts which is after the user guesses
"""
import random  #Used to generate a random item from the theme list

list_of_words_technology=["phone","ipad","mouse","screen","computer","apps","vr"] #List of words


game_session = True
number_of_guesses_technology=len(list_of_words_technology)-1
#Start the game
player_name= input("Enter in your name:") # Ask the player to enter a usename
player_current_score=0
while game_session:
    player_score_tracker={}
    print("Here is everything that could be an answer",list_of_words_technology)
    game_word=random.choice(list_of_words_technology)
    each_letter=[letter for letter in game_word]
    underscores="_ "*len(each_letter)
    print(underscores)
    print("Number of guesses:",number_of_guesses_technology)
    user_guesses=input("Enter in a guess:").lower()
    print(game_word)
    if user_guesses == game_word:
        player_current_score+=1
        print("Correct! The word was: {}. Here is your current score: {}".format(game_word,player_current_score))
        player_score_tracker.update({player_name:player_current_score})
        continue
    else:
        number_of_guesses_technology-=1
        print("You have {} guesses left!".format(number_of_guesses_technology))
        if number_of_guesses_technology==0:
            print("You lost!\n The word was:",game_word)
            game_session = False

