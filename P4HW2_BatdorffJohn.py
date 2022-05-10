# CTI-110
# P4HW2 - Pizza Order
# John Batdorff 
# 4/7/22
#
# The program will ask the user for the number of students eating pizza and how many student will be sharing each pizza
# If the user doesn't input 1.5, 2, or 3 people per pizza, the code will alert the user that their input is invalid.
# The program will ask the user for a new input for number of people per pizza. User will be alerted each time that an invalid input is entered.
# Once the user enters a valid input for number of people per pizza, the program will calculate the number of pizzas that are needed and how much it will cost ($5 per pizza with a 6% sales tax).
# The user will then be displayed the number of students, the number of pizzas needed, and the total cost of it all
# Lastly, the user will be asked if the would like to run the program again. If the user inputs 'y', run the program again, if not, end the program.
#
import math
keep_going = 'y'

while keep_going == 'y':
    students = int(input("How many students do you want to order pizza for?: "))
    people_per_pizza = float(input("Enter number of people per pizza (1.5, 2 or 3): "))
    while people_per_pizza != 1.5 and people_per_pizza != 2 and people_per_pizza != 3:
        print("")
        print("INVALID ENTRY!!!!")
        print("Should have entered 1.5, 2 or 3")
        print("")
        people_per_pizza = float(input('Enter number of people per pizza again. (1.5, 2 or 3): '))
    if people_per_pizza == 1.5 or people_per_pizza == 2 or people_per_pizza == 3:
        x = students / people_per_pizza
        pizzas_needed = math.ceil(x)
        price = pizzas_needed * 5
        total = (price * 0.06) + price
        print("")
        print('----Pizza Order--------')
        print(f'Number of Students : {students}')
        print(f'Pizzas Needed : {pizzas_needed}')
        print(f'Price ${total:.2f}')
        print('--------------------------')
    print('')
    keep_going = input('Would you like to run program again (y for yes): ')
    print('')

    
