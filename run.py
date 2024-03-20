import random

# List of words for Hangman game
list_of_words = ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
              "Lemon", "Peach", "Pear", "Raspberry", "Blueberry", "Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
              "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"]

guesses = []
attempts_left = 6
wrong = 0

# Choose random word from list
random_word = random.choice(list_of_words).upper()

print(random_word)

def print_hangman(wrong):
    """
    Print hangman depending on the number of wrong answers.
    """
    if(wrong == 0):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |          ")
        print("      |          ")
        print("      |          ")
        print("      |          ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 1):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |          ")
        print("      |          ")
        print("      |          ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 2):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |      |   ")
        print("      |      |   ")
        print("      |          ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 3):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |     /|   ")
        print("      |      |   ")
        print("      |          ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 4):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |     /|\\ ")
        print("      |      |   ")
        print("      |          ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 5):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |     /|\\ ")
        print("      |      |   ")
        print("      |     /    ")
        print("      |          ")
        print("     /|\         ")
    elif(wrong == 6):
        print("      ┍——————┑   ")
        print("      |      |   ")
        print("      |      O   ")
        print("      |     /|\\ ")
        print("      |      |   ")
        print("      |     / \\ ")
        print("      |          ")
        print("     /|\         ")
        
    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {attempts_left} guess(es) left")           
        
# Encrypted print of a random word using underscore
for x in random_word:
    guesses.append("_")

    
game_over = False

while not game_over:
    print_hangman(wrong)
    
    user_letter = input("Enter a letter:")
    
    if not user_letter:
        print("That's not a letter. Please enter a letter.")
    else:
        letter = user_letter[0].upper()
        if letter in random_word:
            for x in range(len(random_word)):
                if random_word[x] == letter:
                    guesses[x] = letter
            if "_" not in guesses:
                game_over = True