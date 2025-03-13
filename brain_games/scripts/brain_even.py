from random import randint 
import prompt
from brain_games.cli import welcome_user

def parity_check(number):
    if number % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
def play_even_game():
    print("Welcome to the Brain Games!")
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number=randint(1,20)
    print(f'Question: {random_number}')
    prompt.string('Your answer: ')
    
if __name__ == "__main__":
    play_even_game()