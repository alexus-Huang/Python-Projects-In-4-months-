"""
This game uses:
    Lists - keeps a list of words
    Loops - to either keep the game running or stop the game
    A dictionary - stores player scores
"""
theme=["House","Technology"]
list_of_words_house=["door","floor","roof","kitchen","room","bed","table","sink","bathroom",""]  # List of words
list_of_words_technology=["phone","ipad","mouse","screen","computer","apps","vr"]
player_score_tracker={}

game_session = True
#Start the game
while game_session:
    player_current_score=0
    player_name= input("Enter in your name:") # Ask the player to enter a usename
    player_current_score+=1
    player_score_tracker.update({player_name:player_current_score})
    print(player_score_tracker)

