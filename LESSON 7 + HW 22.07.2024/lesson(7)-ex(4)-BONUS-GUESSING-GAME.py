# LESSON 7 EX 4 BOMUS HW

# GUESSING GAME

# START

import random

cities = ["New York", "Paris", "Tokyo", "Berlin", "Moscow", "Beijing", "London"]

city_to_guess = random.choice(cities).lower()

masked_city = ["_" if char != " " else "-" for char in city_to_guess]

guess_count = 0

print("Welcome to the City Guessing Game!")
print("Try to guess the city name:")
print(" ".join(masked_city))

while "_" in masked_city:
    guess = input("\nGuess a letter: ").lower()

    guess_count += 1

    if guess in city_to_guess:
        for idx, char in enumerate(city_to_guess):
            if char == guess:
                masked_city[idx] = guess
        print("Correct guess!")
    else:
        print("Letter does not exist in the capital.")

    print(" ".join(masked_city))

print(f"\nCongratulations! You've guessed the city '{city_to_guess.title()}' correctly.")
print(f"It took you {guess_count} guesses.")

# END

# Welcome to the City Guessing Game!
# Try to guess the city name:
# _ _ _ _ _ _
#
# Guess a letter: t
# Letter does not exist in the capital.
# _ _ _ _ _ _
#
# Guess a letter: T
# Letter does not exist in the capital.
# _ _ _ _ _ _
#
# Guess a letter: O
# Correct guess!
# _ o _ _ o _
#
# Guess a letter: MOSCOW
# Correct guess!
# _ o _ _ o _
#
# Guess a letter: M
# Correct guess!
# m o _ _ o _
#
# Guess a letter:
# Correct guess!
# m o _ _ o _
#
# Guess a letter: S
# Correct guess!
# m o s _ o _
#
# Guess a letter: C
# Correct guess!
# m o s c o _
#
# Guess a letter: W
# Correct guess!
# m o s c o w
#
# Congratulations! You've guessed the city 'Moscow' correctly.
# It took you 9 guesses.