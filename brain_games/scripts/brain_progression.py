from brain_games.cli import welcome_user,congratulation_message,error_message
from random import randint
import prompt

def play_game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    bandera=False
    contador = 0
    for i in range(3):
        if bandera:
            break
        
        num_inicio = randint(0,100)
        num_incremento = randint(1,5)
        num_fin = num_inicio + (num_incremento*10) # el numero final del ciclo será el valor donde arranca sumandole el incremento por 10 que es el rango de la progresion
        progression_list=[]
        
        for index in range(num_inicio,num_fin,num_incremento):
            progression_list.append(str(index))
        index_unknown_number = randint(0,9) # Buscaremos el indece de un numero aleatorio para preguntar
        correct_answer = progression_list[index_unknown_number]
        progression_list[index_unknown_number] = '..'
        progression_string= ' '.join(progression_list)
        print(f'Question: {progression_string}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            contador += 1
        else:
            error_message(user_answer,correct_answer,name)
            bandera = True

    if contador == 3:
        congratulation_message(name)
    

        

        
        

        


    
            


def main():
    play_game_progression()
