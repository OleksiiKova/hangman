import random
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

list_of_words = {
    "fruit": ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
                    "Lemon", "Peach", "Pear", "Raspberry", "Blueberry"],
    "vegetable": ["Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
                    "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"],
    "animal": ["Elephant", "Tiger", "Giraffe", "Lion", "Zebra", "Kangaroo", "Monkey", "Penguin", "Panda", "Dolphin",
                    "Koala", "Hippo", "Cheetah", "Squirrel", "Crocodile","Ostrich", "Gorilla", "Rhinoceros", "Jaguar", "Buffalo"],
    "country": ["Canada", "Brazil", "Italy", "Australia", "Japan", "Mexico", "Russia", "France", "India", "Spain",
                    "China", "Germany", "Argentina", "Egypt", "Thailand", "Greece", "Vietnam", "Turkey", "Nigeria"],
    "occupation": ["Doctor", "Teacher", "Engineer", "Artist", "Chef", "Pilot", "Scientist", "Musician", "Actor", "Lawyer",
                    "Nurse", "Architect", "Writer", "Dentist", "Journalist", "Programmer", "Photographer", "Veterinarian", "Firefighter", "Banker"],
    "colour": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White", "Brown",
                    "Gray", "Beige", "Cyan", "Magenta", "Teal", "Turquoise", "Lavender", "Maroon", "Indigo", "Violet"]
}

scores_sheet = SHEET.worksheet('scores')
guesses = []
attempts_left = 6
wrong = 0
used_letters = []
random_theme = random.choice(list(list_of_words.keys())) 
random_word = random.choice(list_of_words[random_theme]).upper()

def print_hangman_logo():
    """
    Print hangman logo when the game starts.
    """
    logo = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/   
    """
    print(logo)

def get_user_name():
    """
    Retrieve the user's name and record it in the sheet
    if it doesn't exist yet.
    """
    
    username = input("\nPlease enter your name: \n").upper()
    
    # Check if such a name exists in the game database
    name_column = scores_sheet.col_values(1) 
    if username in name_column:
        # If this name has already been used before, offer to continue the game progress
        print(f"\nName '{username}' is already exists. Do you want to continue the progress? (Y/N)")
        while True:
            user_choice = input("").upper()
            if user_choice == "Y":
                start_menu(username)
                break
            if user_choice == "N":
                get_user_name()
                break
            else:
                print("To make choice, enter 'Y' or 'N'!")
                continue
    else:
        # If this name has not been used before, add this username to the game database
        scores_sheet.append_row([username,0])
    return username

def start_menu(username):
    """
    Main menu, where the user can select what wants to do: 
    (start the game, check the leaderboard or change a user)
    """
    while True:
        print(f"\n{username}, TO CONTINUE PLEASE ENTER:")
        print("1 - START A NEW GAME")
        print("2 - CHECK THE LEADERBOARD")
        print("3 - CHANGE A USER")
        print("4 - READ THE RULES")
        start_input = input("")
        if start_input == "1":
            game(username, guesses, attempts_left, wrong, random_word)
            break
        elif start_input == "2":
            print_leaderboard(username)
            break
        elif start_input == "3":
            main()
        elif start_input == "4":
            print_rules(username)
        else:
            print("\nPlease enter the correct input!")
            start_menu(username)    

def game(username, guesses, attempts_left, wrong, random_word):
    """
    Start the Hangman game.
    """    
    print(random_word)
    
    # Encrypt the random word using underscores
    for x in random_word:
        guesses.append("_")
    
    while attempts_left > 0:
        print_hangman(wrong)
        print_info_about_hidden_word(guesses, random_theme, attempts_left)
        user_letter = get_user_letter(used_letters)
        
        # If the entered letter is in the hidden word    
        if user_letter in random_word:
            for x in range(len(random_word)):
                if random_word[x] == user_letter:
                    guesses[x] = user_letter
            print(f"Correct! There's letter '{user_letter}' in this word!")
            
            # Check if all letters in the hidden are open
            if "_" not in guesses:
                print(f"\nCONGRATULATIONS {username}, YOU WON!")
                print(f"THE WORD WAS {random_word}!")
                new_score = update_score(username)             
                print(f"YOUR TOTAL SCORE: {new_score} point(s)!")
                data_reset()
                start_menu(username)
        
        # If the entered letter isn't in the hidden word           
        else: 
            attempts_left -= 1
            wrong += 1
            print(f"Sorry, there's no letter '{user_letter}' in this word!")
            
    # If all attempts are exhausted the game ends
    if wrong == 6:
        print_hangman(wrong)
        print(f"\n{username}, YOU LOST! THE WORD WAS {random_word}!")
        data_reset()
        start_menu(username) 

def get_user_letter(used_letters):
    """
    Get input from the user and validate it.
    """
    while True:
        try:
            user_input = input("Enter a letter: \n").upper()
            # Check is it a letter
            if not user_input.isalpha():
                raise ValueError("That's not a letter!")
            # Check is this letter entered for the first time
            elif user_input in used_letters:
                raise ValueError("You've already entered this letter!")
            # Check is it entered just one letter
            elif len(user_input) != 1:
                raise ValueError("Please enter just one letter!")
            else:
                # If the conditions above are met, add the letter to the list of already entered letters
                used_letters.append(user_input)
                return user_input
        except ValueError as e:
            print(f"\n{e}")

def print_hangman(wrong):
    """
    Print hangman depending on the number of wrong answers.
    """
    print("----------------------------")
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
        
def print_info_about_hidden_word(guesses, random_theme, attempts_left):
    """
    Print message about hidden word: 
    topic, quantity underscores, attemts left.
    """
    # What topic the word relates to
    print(f"The hidden word is {random_theme}!")
    
    # How many underscores need to print
    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
        
    # How many attemts left
    print(f"\nYou have {attempts_left} guess(es) left.")           
    
def data_reset():
    """
    Reset the data before a new game.
    """
    global guesses, attempts_left, wrong, used_letters, random_word, random_theme
    
    random_theme = random.choice(list(list_of_words.keys())) 
    random_word = random.choice(list_of_words[random_theme]).upper()
    guesses = []
    attempts_left = 6
    wrong = 0
    used_letters = [] 

def update_score(username):
    """
    Get the score from the sheet and 
    update score when the user guessed the word.
    """
      
    # Get the existing data about the player from the game database
    name_column = scores_sheet.col_values(1)
    score_column = scores_sheet.col_values(2)
    user_index = name_column.index(username) + 1
    current_score = int(score_column[user_index - 1])
    
    # Update scores in the gama database
    new_score = current_score + 1  
    scores_sheet.update_cell(user_index, 2, str(new_score))
    
    return new_score

def print_leaderboard(username):
    """
    Print the leaderboard, sorted by decreasing scores.
    """
    print("")
    # Get all the data from the game database sheet
    all_rows = scores_sheet.get_all_values()
    
    # Sort by decreasing points
    data = [(row[0], int(row[1]) if i != 0 else row[1]) for i, row in enumerate(all_rows)]
    sorted_data = sorted(data[1:], key=lambda x: x[1], reverse=True)
    print(tabulate(sorted_data, headers=["Name", "Score"]))
    start_menu(username)

def print_rules(username):
    rules = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*     Rules of the Hangman game:                                          *
*  1. The objective of the game is to guess the secret word               *
*  2. The secret word is displayed as a series of underscores, each       *
*     representing a letter in the word.                                  *
*  3. The secret word can be on a different themes. The topic displayed   *
*     under the gallows. For example: "The hidden word is fruit!".        *
*  4. The player guess one letter at a time. If the guessed letter is     *
*     in the secret word, all occurrences of that letter are revealed in  *
*     the word. Otherwise, a part of the hangman is drawn and the player  *
*     loses one attempt.                                                  *
*  5. The player has 6 attempts to guess the entire word.                 *
*  6. The player wins if they successfully guess all the letters in the   *
*     secret word before running out of attempts.                         *
*  7. After the game ends, the player may have the option to play         *
*     again with a new word.                                              *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"""
    print(rules)
    start_menu(username)
      
def main():
    """
    Main function to run the programm.
    """
    print_hangman_logo()   
    print("WELCOME TO THE HANGMAN GAME!")  
    username = get_user_name()
    start_menu(username)
   
main()