# CTI-110
# P3HW2 - Pizza Order
# John Batdorff 
# 3/24/22
#
# This program will ask the user to input how many students will be eating pizza and how many students will be sharing each pizza.
# If the user inputs anything other than 1.5, 2, or 3 students per pizza, display an error to the user and tell them to run the program again.
# If the user inputs 1.5, 2, or 3, calculate the number of pizzas needed. Each pizza is to be assumed to cost $5 with a %6 sales tax at the end of the purchase.
# Based on the users input, you will either display and error OR the correct information about the number of pizzas needed and how much it will cost.
#
import math

students = int(input("How many students do you want to order pizza for?: "))
people_per_pizza = float(input("Enter number of people per pizza (1.5, 2 or 3): "))

if people_per_pizza == 1.5:
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
elif people_per_pizza == 2:
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
elif people_per_pizza == 3:
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
else:
    print("")
    print("INVALID ENTRY!!!!")
    print("Should have entered 1.5, 2 or 3")
    print("")
    print("Run Program again")
    
