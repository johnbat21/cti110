# CTI-110
# P5HW2 - Math Quiz
# John Batdorff
# 4/28/22
#
# This program randomly generates a math quiz for the user
# Using random number generators, create two functions. One will be an addition question and the second will be a substraction question.
# The user will be given the opportunity to answer and will be prompted if they answer right or wrong.
# Second part of the program will create a menu for the user to choice which type question they would to answer.
# The first option in the menu will be for the addition question, the secons option will be for the subtraction question, and the third/final option will terminate the program
# If the user chooses any option other than these three, prompt the user that their choice in invalid then display the menu again.
import random

print("Welcome to Math Quiz")
print('')

def addition():
    random1 = random.randint(0,300)
    random2 = random.randint(0,300)
    print(random1)
    print('+',random2)
    print('')
    print('Enter answer')
    answer = random1 + random2
    user_answer = int(input())
    if answer == user_answer:
        print('Congratulations!!!! Your answer is correct.')
    else:
        print('Sorry, your guess is not correct.')
        print(f'The correct answer is {answer}')
    

def subtraction():
    random1 = random.randint(0,300)
    random2 = random.randint(0,300)
    print(random1)
    print('-',random2)
    print('')
    print('Enter answer')
    answer = random1 - random2
    user_answer = int(input())
    if answer == user_answer:
        print('Congratulations!!!! Your answer is correct.')
    else:
        print('Sorry, your guess is not correct.')
        print(f'The correct answer is {answer}')
    

def display_menu():
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')
    

def main():
    keep_going = 'y'
    while keep_going == 'y':
        display_menu()
        choice = int(input('Please choose one of the menu options: '))
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            keep_going = 'n'
            print('Thank you for playing...')
            print('Bye!!')
        else:
            print('That is not an option for this menu.')
            print('Please enter 1, 2, or 3.')
            print('')

        
main()
    

