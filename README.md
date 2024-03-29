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

### Rules of the game

If the user is not familiar with the rules of the game, he can read them by selecting the required menu item.

![Rules](readme_images/rules.png)

### Leaderboard

User can check the game's leaderboard to see their position among other participants.

![Leaderboard](/readme_images/leaderboard.png)

### Game

![Game](/readme_images/game.png)

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
