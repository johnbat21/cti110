# This program will calculate the number of pizzas you need to order for a group of students.
# 2/15/22
# CTI-110 P1HW2 - Pizza Order
# John Batdorff
#
students = int(input("How many students do you want to order pizza for?"))
pizza_slices = students * 6
pizzas_needed = pizza_slices / 2
print()
print("--------Pizza Order--------")
print("Number of Students: ", students)
print("Pizza Slices Needed: ", pizza_slices)
print("Pizzas Needed: ", pizzas_needed)
print("---------------------------")
