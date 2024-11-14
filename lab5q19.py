#question 19

gello
import random 
 
def guess_the_number(): 
    
    number_to_guess = random.randint(1, 100) 
    guess = None 
 
    print("Welcome to the Guess the Number game!") 
    print("I have selected a number between 1 and 100. Can you guess it?") 
 

    while guess != number_to_guess: 
        try: 
            
            guess = int(input("Enter your guess: ")) 
             
             
            if guess < number_to_guess: 
                print("Too low! Try again.") 
            elif guess > number_to_guess: 
                print("Too high! Try again.") 
            else: 
                print("Congratulations! You've guessed the number!") 
        except ValueError: 
            print("Please enter a valid integer.") 
 
 
guess_the_number() 
