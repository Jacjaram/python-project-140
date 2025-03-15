from brain_games.cli import welcome_user,error_message,congratulation_message
from random import randint
import prompt

def play_calc_game():
    name=welcome_user()
    print('What is the result of the expression?')
    contador=0
    bandera=False
    for i in range(3):
        if bandera:
            break
        arithmetic_symbols = ['+','-','*']
        select_symbol=arithmetic_symbols[randint(0,2)]
        number1=randint(0,100)
        number2=randint(0,100)
       
        print(f'Question: {number1} {select_symbol} {number2}')
        user_answ=prompt.integer('Your answer: ')
        if select_symbol == '+':
            if (number1 + number2) == user_answ:
                print('Correct!')
            else:
                error_message(user_answ,number1+number2,name)
                bandera=True
                break
        elif select_symbol == '-':
            if (number1 - number2) == user_answ:
                print('Correct!')                
            else:
                error_message(user_answ,number1 - number2, name)
                bandera=True
                break
        elif select_symbol == '*':
            if (number1 * number2) == user_answ:
                print('Correct!')
            else:
                error_message(user_answ,number1 * number2, name)
                bandera=True
                break
        else:
            if (number1 / number2) == user_answ:
                print('Correct!')
            else:
                error_message(user_answ,number1 / number2, name)
                bandera=True
                break
        
        contador+=1
    if contador == 3:
        congratulation_message(name)

def main():
    play_calc_game()