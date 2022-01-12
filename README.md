# Guess the US States
Name as many US states as possible by looking at the map of the US.

## Setup
Clone this repository to a local directory. Refer to [GitHub Pages](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for more guidance.

Next, you should install the package neccessary to run **main.py**: *turtle,* and *pandas*. You can install these using **pip**:
```
- pip install turtle
```
```
- pip install pandas
```

Now your setup is complete!

## Running the Code
To run the code, run **main.py**. This will open up the turtle window and display the US map.

![US map](https://github.com/BhumikGangwani/Guess-the-US-States/blob/master/blank_states_img.gif)

A dialog box will also pop up when you run the code. You should enter the names of the States in this box. For every correct guess, the map will be updated and state you guessed will be marked by it's name. The score on the dialog box will also get updated with every correct guess.

You can enter "Exit" in the dialog box when you are finished playing the game. This will update the "states_to_learn.csv" file with the names of the states that you didn't guess in you previous attempt.

That's pretty much all the information you need to play the game.

## Future plans
- Add more maps to the game and let the user choose what they'd like to play.
- Introduce new difficulty levels including limited number of guesses and a countdown timer.
