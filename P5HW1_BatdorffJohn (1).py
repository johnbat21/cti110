# CTI-110
# P5HW1 - Score List
# John Batdorff
# 4/26/22
#
# This program creates multiple functions for the user to call.
# The first function collects all of the scores that the user would like to input.
# The second function drops the lowest score, determines the average, and the letter grade.
# The second part of the program will create a menu with a 3 options for the user to choose from.
# The first option calls the function that creates the list.
# The second options call the fucntion that displays the results of the list.
# If no list has been created, display to the user that no list has been created and display the menu again.
# The third and final option ends the program but only ends the program when it is selected.

def collect_scores(scores):
    number_scores = int(input("How many scores would you like to enter?: "))
    
    print("")
    for i in range(number_scores):
        score_input = int(input(f'Enter score #{i + 1}: '))
        while score_input < 0 or score_input > 100:
            print('')
            print('INVLAID Score entered!!!!')
            print('Scores should be between 0 and 100')
            score_input = int(input(f'Enter score #{i + 1} again: '))
        scores.append(score_input)
    return scores

def display_scores(scores):
    lowest = min(scores)
    scores.remove(lowest)
    average = sum(scores)/len(scores)

    print('--------------Results-----------')
    print('Lowest Score  :', lowest)
    print('Modified List :', scores)
    print('Scores Average:', average)

    if average >= 90:
        print('Grade         : A')
        print('--------------------------------')
    elif average >= 80:
        print('Grade         : B')
        print('--------------------------------')
    elif average >= 70:
        print('Grade         : C')
        print('--------------------------------')
    elif average >= 60:
        print('Grade         : D')
        print('--------------------------------')
    else:
        print('Grade         : F')
        print('--------------------------------')

def display_menu():
    print('-----------MENU-------------')
    print('1) Create Score List')
    print('2) Display Results')
    print('3) Exit')
    print('----------------------------------')
    print('')


def main():
    scores = []
    keep_going = 'y'
    while keep_going == 'y':
        display_menu()
        choice = int(input('Enter choice: '))
        if choice == 1:
            scores = collect_scores(scores)
        elif choice == 2:
            if len(scores) == 0:
                print('Create list first')
            else:
                display_scores(scores)
        elif choice == 3:
            keep_going = 'n'
            print('Program terminating....')
            print('Good Bye!')
        else:
            print('')
            print('INVALID choice entered !!!!!')
            print('Choose from the menu options please')
            print('')

main()
   

