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

scores_sheet = SHEET.worksheet('scores')

# List of words for Hangman game
# list_of_words = ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
#               "Lemon", "Peach", "Pear", "Raspberry", "Blueberry", "Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
#               "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"]

list_of_words = {
    "fruit": ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
                    "Lemon", "Peach", "Pear", "Raspberry", "Blueberry"],
    "vegetable": ["Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
                    "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"],
    "animal": ["Elephant", "Tiger", "Giraffe", "Lion", "Zebra", "Kangaroo", "Monkey", "Penguin", "Panda", "Dolphin",
                    "Koala", "Hippo", "Cheetah", "Squirrel", "Crocodile","Ostrich", "Gorilla", "Rhinoceros", "Jaguar", "Buffalo"],
    "country": ["Canada", "Brazil", "Italy", "Australia", "Japan", "Mexico", "Russia", "France", "India", "Spain",
                    "China", "Germany", "Argentina", "Egypt", "Thailand", "Greece", "Vietnam", "South Africa", "Turkey", "Nigeria"],
    "occupation": ["Doctor", "Teacher", "Engineer", "Artist", "Chef", "Pilot", "Scientist", "Musician", "Actor", "Lawyer",
                    "Nurse", "Architect", "Writer", "Dentist", "Journalist", "Programmer", "Photographer", "Veterinarian", "Firefighter", "Banker"],
    "colour": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White", "Brown",
                    "Gray", "Beige", "Cyan", "Magenta", "Teal", "Turquoise", "Lavender", "Maroon", "Indigo", "Violet"]
}

guesses = []
attempts_left = 6
wrong = 0
used_letters = []
random_theme = random.choice(list(list_of_words.keys())) 
random_word = random.choice(list_of_words[random_theme]).upper()
username = ""
new_score = ""

def print_hangman_logo():
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

def get_user_letter():
    """
    Get input from еру user and validate it.
    """
    while True:
        user_input = input("Enter a letter: \n").upper()
        
        if not user_input.isalpha() :
            print("That's not a letter. Please, enter a letter!")
        elif user_input in used_letters:
            print("You've already entered this letter. Please, enter another letter!")
        elif len(user_input) != 1:
            print("Please enter just one letter!")
        else:
            used_letters.append(user_input)
            return user_input

def print_hangman():
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
        
def print_attempts_left():
    """
    Print message how many attempts left
    """
    print(f"The hidden word is {random_theme}!")
    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {attempts_left} guess(es) left.")           
      
def game():
    """
    Start the Hangman game 
    """
    global wrong, attempts_left, username, name_column, score_column, new_score
    
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
                print("\nCONGRATULATIONS, YOU WON!")
                print(f"THE WORD WAS {random_word}!")
                update_score()              
                print(f"YOUR TOTAL SCORE: {new_score} point(s)!")
                data_reset()
                start_menu() 
        else: 
            attempts_left -= 1
            wrong += 1
            print(f"Sorry, there is no letter '{user_letter}' in this word!")

    if wrong == 6:
        print_hangman()
        print(f"\nYOU LOST! THE WORD WAS {random_word}!")
        data_reset()
        start_menu() 
    
def start_menu():
    """
    Main menu, where the user can select what wants to do: 
    (start the game, check the leaderboard or change a user)
    """
    while True:
        print(f"\n{username}, to continue please enter:")
        print("1 START A NEW GAME")
        print("2 CHECK THE LEADERBOARD")
        print("3 CHANGE A USER")
        start_input = input("")
        if start_input == "1":
            game()
            break
        elif start_input == "2":
            print_leaderboard()
            break
        elif start_input == "3":
            main()
        else:
            print("\nPlease enter the correct input")
            start_menu()

def data_reset():
    """
    Reset the data before new game.
    If the game will run without restart the program.
    """
    global guesses, attempts_left, wrong, used_letters, random_word, random_theme
    random_theme = random.choice(list(list_of_words.keys())) 
    random_word = random.choice(list_of_words[random_theme]).upper()
    guesses = []
    attempts_left = 6
    wrong = 0
    used_letters = []

def get_user_name():
    """
    Get user name and record it in the sheet, 
    if there is no such name yet.
    """
    global username
    username = input("\nPlease, enter your name: \n")
    name_column = scores_sheet.col_values(1)
    if username in name_column:
        print(f"\nName {username} is already exists. Do you want to continue the progress? (Y/N)")
        
        def validate_user_choice():
            user_choice = input("").upper()
            if user_choice == "Y":
                start_menu()
            if user_choice == "N":
                get_user_name()
            else:
                print("To make choice, enter 'Y' or 'N'!")
                validate_user_choice()
        validate_user_choice()
    else:
        scores_sheet.append_row([username,0])
    return username

def update_score():
    """
    Get the score from the sheet and 
    update score when the user guessed the word.
    """
    global name_column, score_column, new_score
    name_column = scores_sheet.col_values(1)
    score_column = scores_sheet.col_values(2)
    
    user_index = name_column.index(username) + 1
    current_score = int(score_column[user_index - 1])
    new_score = current_score + 1
    scores_sheet.update_cell(user_index, 2, str(new_score))

def print_leaderboard():
    """
    Print leaderboard, sorted by descending scores.
    """
    print("")
    all_rows = scores_sheet.get_all_values()
    data = [(row[0], int(row[1]) if i != 0 else row[1]) for i, row in enumerate(all_rows)]
    sorted_data = sorted(data[1:], key=lambda x: x[1], reverse=True)
    print(tabulate(sorted_data, headers=["Name", "Score"]))
    start_menu()
      
def main():
    print_hangman_logo()   
    print("WELCOME TO THE HANGMAN GAME!") 
    get_user_name()
    start_menu()
    

main()