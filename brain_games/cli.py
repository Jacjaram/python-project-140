import prompt

def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def error_message(user,correct,name):
    print(f"'{user}' is wrong answer ;(. Correct answer was '{correct}'. \nLet's try again, {name}!")

def congratulation_message(name):
    print(f'Congratulations, {name}!')
