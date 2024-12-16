# Write a Python program for a number guessing game where the 
# user has to guess a number between 1 and 50. The program should 
# also check if the guessed number is prime. Use a ‘while loop’ for 
# the guessing game and a ‘for loop’ to check if a number is prime.

class PrimeOrNot:
    def __init__(self):
        print("Welcome to the game!")
        print("Guess the correct prime number between 1 and 50 to win!")
        self.correct_number = 29  

    def is_prime(self,num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def game(self):
        while True:
            try:
                guess = int(input("Guess a number between 1 and 50: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if guess < 1 or guess > 50:
                print("Number out of range. Try again.")
                continue

            if self.is_prime(guess):
                print(f"{guess} is a prime number.")
                if guess == self.correct_number:
                    print("Congratulations! You guessed the correct prime number.")
                    break
                else:
                    print("That's a prime number, but not the correct one.")
            else:
                print(f"{guess} is not a prime number.")

            print("Try again!")

game = PrimeOrNot()
game.game()
