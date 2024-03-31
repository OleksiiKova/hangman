# The Hangman

Hangman is a popular game that was played with pen and paper before the era of computer technology. This is now possible thanks to the use of digital implementations on computers and mobile devices. It's a fun way to test vocabulary, spelling, and deduction skills.

## Technologies

1. lucid.app - to create a flowchart.
2. VSCode - to write Python code.
3. GitHub - to store the project's code.
4. Heroku - to deploy my application.

## Features

### Welcome block

The player is presented with a welcome screen and prompted to enter a name.

![Welcome](readme_images/welcome.png)

The program verifies if there is a player with the same name already registered. If found, it prompts whether you would like to resume your progress.

![CheckName](readme_images/check_name.png)

### Menu

After entering a name, the user is presented with a selection of further actions. He can start the game, view the leaderboard, read the rules, or change the username.

![Menu](readme_images/menu.png)

### Game

The secret word may relate to such topics: fruit, vegetable, animal, country, occupation and color. The topic displayed under the gallows. Underneath the user can see the underscores where the letters will populate with correct guesses and below this is where they will see the number of how many guesses left.

![Game](readme_images/game.png)

### Leaderboard

Users can check the game's leaderboard to see their position among other participants.

![Leaderboard](readme_images/leaderboard.png)

### Finish game

On completion of the game, win or lose, the user is given the start menu options.

![Win](readme_images/win.png)

![Finish](readme_images/game_over.png)

### Rules of the game

If the user is not familiar with the rules of the game, he can read them by selecting the required menu item.

![Rules](readme_images/rules.png)

## Testing

### Manual testing

| Feature tested                                          | Expected outcome                                                                                                                                      | Actual outcome |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Enter name.                                             | The program verifies if there is a player with the same name already registered. If found, it prompts whether you would like to resume your progress. | As expected.   |
| In the start menu enter not 1, 2, 3 or 4.               | The message appears: "Please enter the correct input                                                                                                  | As expected.   |
| In the start menu enter 1.                              | The game starts.                                                                                                                                      | As expected.   |
| In the start menu enter 2.                              | Print the actual leaderboard.                                                                                                                         | As expected.   |
| In the start menu enter 3.                              | Print the rules.                                                                                                                                      | As expected.   |
| In the start menu enter 4.                              | Print enter your name.                                                                                                                                | As expected.   |
| In the game enter a number or symbol.                   | The message appears: "That's not a letter!" and ask again to enter the letter.                                                                        | As expected.   |
| In the game enter several letters.                      | The message appears: "Please enter just one letter!" and ask again to enter the letter.                                                               | As expected.   |
| In the game enter letter that has already been entered. | The message appears: "You've already entered this letter!" and ask again to enter the letter.                                                         | As expected.   |
| Enter letter which is in the secret word. | The letter(s) appears instead of an underscore(s).| As expected. |
| Enter letter which is not in the secret word. | A part of the hangman is drawn and the player loses one attempt. | As expected. |
| After 6 incorrect guesses.| The drawing is completely ready and the game ends. You lose. | As expected. |
| If there are no more underscores left. | The game ends, you won. The player's score increases by 1. | As expected. |


## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

Then create a _Config Var_ called `PORT`. Set this to `8000`

Create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
