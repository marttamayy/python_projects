import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
--------------------------------------------------------    
 __          __  _                            _        
 \ \        / / | |                          | |       
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
  _ \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |
 | | \/ |\/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __        
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \       
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |      
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|      
                      __/ |                            
                     |___/                             
---------------------------------------------------------
      ''')

lives = 6 # 6 tries
print(stages[lives])

word_list = [
    "apple",      # Fruit
    "car",        # Vehicle
    "dog",        # Animal
    "ocean",      # Nature
    "balloon",    # Party
    "book",       # Object
    "piano",      # Music
    "rainbow",    # Nature
    "cactus",     # Plant
    "pizza",      # Food
    "moon",       # Space
    "robot",      # Technology
    "beach",      # Place
    "guitar",     # Music
    "sunflower",  # Plant
    "castle",     # Place
    "train",      # Vehicle
    "cookie",     # Food
    "teddy",      # Toy
    "jungle"      # Place
]

end_of_game = False


chosen_word = random.choice(word_list) # randomly chooses a word from the list

word_length = len(chosen_word) # length of chosen word

#print(f"The word is {chosen_word} and the length is {word_length}")

display = []

for letter in chosen_word: # creates display for the word using '_'
    display.append('_')

print(display)


str_display = ""
guessed = False

letters_guessed = ""

while str_display != chosen_word and end_of_game == False: # while the display and chosen word are not the same the loop keeps going

    guess = input("Guess a letter: ").lower()

    counter = 0

    if letters_guessed == "":
        letters_guessed = letters_guessed + guess
    else:
        letters_guessed = letters_guessed + ", " + guess
    
    while counter < len(chosen_word):
        if chosen_word[counter] == guess:
            display[counter] = guess
            counter += 1
            guessed = True
        else:
            counter += 1
            

    if guessed == False:
        lives -= 1
        if lives >0:
            print("Oops. You lost 1 life.")
    else:
        guessed = False

    if lives == 0:
        print("YOU LOST.")
        end_of_game = True # end of the game because you lost

    str_display = ''.join(display)

    print(stages[lives])
    print(f"You have used {letters_guessed}")
    print(f"You have {lives} lives.")
    print(display)


if lives > 0:
    print(f"The word is {str_display}:. YOU WON!")
else: 
    print(f"The word is {chosen_word}")

