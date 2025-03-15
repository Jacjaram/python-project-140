from brain_games.cli import welcome_user, error_message, congratulation_message
import math
from random import randint
import prompt

def is_prime(number):
    if number <= 1:
        return 'no'
    if number <= 3:
        return 'yes'
    if number % 2 == 0 or number % 3 == 0:
        return 'no'
        
    for i in range(5, int(math.sqrt(number)) + 1, 2):  
        if number % i == 0:
            return 'no'
    return 'yes'

def play_game_prime():
    name=welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    contador = 0
    bandera = False
    for i in range(3):
        if bandera:
            break
        number = randint(0,100)
        print(f'Question: {number}') 
        user_answer = prompt.string('Your answer: ')
        correct_answer = is_prime(number)
        
        if user_answer == correct_answer:
            print('Correct!')
            contador += 1
        else:
            error_message(user_answer,is_prime(number),name)
            bandera = True
    
    if contador == 3:
        congratulation_message(name)
        
def main():
    play_game_prime()