import random

# List of words for Hangman game
list_of_words = ["Apple", "Banana", "Orange", "Pineapple", "Strawberry", "Watermelon", "Mango", "Grape", "Cherry", "Kiwi", 
              "Lemon", "Peach", "Pear", "Raspberry", "Blueberry", "Carrot", "Potato", "Tomato", "Cucumber", "Broccoli", 
              "Spinach", "Lettuce", "Pepper", "Onion", "Garlic", "Cauliflower", "Zucchini", "Eggplant", "Pumpkin", "Radish"]

guesses = []
attempts_left = 6
wrong = 0
used_letters = []


# Choose random word from list
random_word = random.choice(list_of_words).upper()

print("WELCOME TO THE HANGMAN GAME!")

def get_user_letter():
    while True:
        user_letter = input("Enter a letter: \n").upper()
        
        if not user_letter.isalpha() :
            print("That's not a letter. Please, enter a letter!")
        elif user_letter in used_letters:
            print("You have already entered this letter. Please, enter another letter!")
        elif len(user_letter) != 1:
            print("Please enter just one letter!")
        else:
            return user_letter

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
        
    print("Word: ", end='')
    for element in guesses:
        print(f"{element} ", end='')
    print(f"\nYou have {attempts_left} guess(es) left")           
    
      
def main():
    print(random_word)
    
    global wrong
    global attempts_left
    
    # Encrypted print of a random word using underscore
    for x in random_word:
        guesses.append("_")

    while attempts_left > 0:
        print_hangman()
        
        user_letter = get_user_letter()
        
        used_letters.append(user_letter)
            
        if user_letter in random_word:
            for x in range(len(random_word)):
                if random_word[x] == user_letter:
                    guesses[x] = user_letter
            if "_" not in guesses:
                print("Congratulations, you won!")
                print(f"The word was {random_word}!")
                break
        else: 
            attempts_left -= 1
            wrong += 1
            print("Sorry, there is no such letter in this word!")

    if wrong == 6:
        print_hangman()
        print(f"Game Over!")
        print(f"Sorry, you lost. The word was {random_word}!")
    
      
main()