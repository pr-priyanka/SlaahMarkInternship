import time

def custom_random(seed):
    """Generate a pseudo-random number using a simple linear congruential generator."""
    seed = (1103515245 * seed + 12345) & 0x7FFFFFFF
    return seed

def random_number(min_val, max_val, seed):
    """Generate a random number between min_val and max_val using custom_random."""
    return min_val + custom_random(seed) % (max_val - min_val + 1)

def play_game():
    try:
        name = input("May I ask you for your name? ")
        print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
        seed = int(time.time())  # Use current time as seed for randomness
        number_to_guess = random_number(1, 200, seed)
        attempts = 0

        while True:
            try:
                guess = int(input("Go ahead. Guess!\nGuess: "))
                attempts += 1
                if guess < number_to_guess:
                    print("The guess of the number that you have entered is too low")
                elif guess > number_to_guess:
                    print("The guess of the number that you have entered is too high")
                else:
                    print(f"Congratulations {name}! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")

        print(f"The number I was thinking of was {number_to_guess}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        while True:
            play_game()
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again not in ("yes", "y"):
                print("Thanks for playing! Goodbye!")
                break
    except Exception as e:
        print(f"An error occurred in the main loop: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
