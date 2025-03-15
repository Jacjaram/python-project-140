from brain_games.cli import welcome_user,error_message,congratulation_message
import prompt
from random import randint

def play_game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    bandera = False
    contador = 0

    for i in range(3):
        if bandera:
            break
        num1 = randint(1,100)
        num2 = randint(1,100)   

        if num1<num2:
            aux = num2
            num2 = num1
            num1 = aux

        print(f'Question: {num1} {num2}')
        
        while (num1%num2 != 0):        
            aux = num2
            num2 = num1%num2
            num1 = aux       
        
        user_answer = prompt.integer('Your answer: ')

        if user_answer == num2:
            print('Correct!')
        else:
            return error_message(user_answer,num2,name)
            bandera=True
        contador += 1
    if contador == 3:
        return congratulation_message(name)
def main():
    play_game_gcd()

