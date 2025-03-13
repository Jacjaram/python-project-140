from random import randint 
import prompt
from brain_games.cli import welcome_user

def parity_check(number):
    if number % 2 == 0:
        return 'yes' # Es par
    else:
        return 'no' # No es par, es impar
    
def play_even_game():
    print("Welcome to the Brain Games!")
    name=welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0,3):    
        random_number=randint(1,20)
        print(f'Question: {random_number}')        
        user_answ=prompt.string('Your answer: ')
        if user_answ == parity_check(random_number):
            print('Correct!')
        else:
            print(f"'{user_answ}' is wrong answer ;(. Correct answer was '{parity_check(random_number)}'. \nLet's try again, {name}!")
            break
        print(f'Congratulations, {name}!')


def main():
    play_even_game()  
# if __name__ == "__main__":
#     play_even_game()