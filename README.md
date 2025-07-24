# Guess-the-states-
# 🗺️ U.S. States Guessing Game 🇺🇸

Game to guess the 50 USA states.....hopefully i'll update it with time constriction
This is a Python-based interactive game that challenges users to guess all 50 U.S. states. It uses the Turtle Graphics module to display a blank U.S. map and pandas to manage the list of states and their coordinates.

---

## 📌 How It Works

- A blank U.S. map is displayed using Turtle graphics.
- The player is prompted to guess the name of a U.S. state.
- If the guess is correct:
  - The name of the state is displayed at its location on the map.
  - The guess count increases.
- The game continues until all 50 states are guessed or the player exits.
- If the user types nothing or closes the prompt, the game ends and a CSV file `states_to_learn.csv` is generated, listing the states that were not guessed.
