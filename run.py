import random

# List of words for Hangman game
list_of_words = ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
              "Lemon", "Peach", "Pear", "Raspberry", "Blueberry", "Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
              "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"]

guesses = []
attempts_left = 6
wrong = 0
used_letters = []
random_word = random.choice(list_of_words).upper()

def get_user_letter():
    """
    Get input from еру user and validate it.
    """
    while True:
        user_input = input("Enter a letter: \n").upper()
        
        if not user_input.isalpha() :
            print("That's not a letter. Please, enter a letter!")
        elif user_input in used_letters:
            print("You have already entered this letter. Please, enter another letter!")
        elif len(user_input) != 1:
            print("Please enter just one letter!")
        else:
            used_letters.append(user_input)
            return user_input

def print_hangman():
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
        
def print_attempts_left():
    """
    Print message how many attempts left
    """
    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {attempts_left} guess(es) left")           
      
def game():
    """
    Start the Hangman game 
    """
    global wrong
    global attempts_left
    
    print(random_word)
    
    # Encrypt the random word using underscores
    for x in random_word:
        guesses.append("_")
    
    while attempts_left > 0:
        print_hangman()
        print_attempts_left()
        
        user_letter = get_user_letter()
            
        if user_letter in random_word:
            for x in range(len(random_word)):
                if random_word[x] == user_letter:
                    guesses[x] = user_letter
            if "_" not in guesses:
                print("")
                print("CONGRATULATIONS, YOU WON!")
                print(f"THE WORD WAS {random_word}!")
                data_reset()
                start_menu() 
        else: 
            attempts_left -= 1
            wrong += 1
            print("Sorry, there is no such letter in this word!")

    if wrong == 6:
        print_hangman()
        print("")  
        print(f"YOU LOST! THE WORD WAS {random_word}!")
        print(f"GAME OVER!")
        data_reset()
        start_menu() 
    
def start_menu():
    """
    Main menu, where the user can select what wants to do: 
    start the game or see the leaderboard.
    """
    print("Enter 1 to start new game")
    print("Enter 2 to display the leaderboard")
    start_input = int(input())
    if start_input == 1:
        game()
    elif start_input == 2:
        pass
    else:
        print("Please enter 1 or 2")
        start_menu()

def data_reset():
    """
    Reset the data before new game.
    If the game will run without restart the program.
    """
    global guesses
    global attempts_left
    global wrong
    global used_letters
    global random_word
    random_word = random.choice(list_of_words).upper()
    guesses = []
    attempts_left = 6
    wrong = 0
    used_letters = []

def main():
    print("WELCOME TO THE HANGMAN GAME!")
    print("")
    
    start_menu()

main()