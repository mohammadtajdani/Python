import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Ask the user to choose a difficulty level
level = input("Please choose your level (High, Medium, Low): ").capitalize()

# Set the number of attempts based on the chosen difficulty
if level == 'High':
    max_attempts = 7
elif level == 'Medium':
    max_attempts = 15
elif level == 'Low':
    max_attempts = 20
else:
    # Default attempts if input is invalid
    max_attempts = 25

# Initialize remaining chances
remaining_chances = max_attempts

# Game loop
for attempt in range(max_attempts):
    print(f"You have {remaining_chances} chance(s) left.")
    
    # Ask user to guess a number
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    
    # Check the user's guess
    if guess > number_to_guess:
        print("Your guess is too HIGH.")
    elif guess < number_to_guess:
        print("Your guess is too LOW.")
    else:
        print("🎉 Congratulations! You WIN! 🏆")
        break  # Exit the loop if guessed correctly
    
    # Decrease the remaining chances
    remaining_chances -= 1
    
    # If no chances left, user loses
    if remaining_chances == 0:
        print(f"💔 You LOSE! The correct number was {number_to_guess} 😢")
        break
