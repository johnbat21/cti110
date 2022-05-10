# CTI-110
# P4HW1 - Score List
# John Batdorff
# 4/5/22
#
# This code will ask the user how many scores they would like to enter in.
# The program will then create a list that will contain each score entered.
# The program will check each score as it is entered to make sure it is a valid entry (0-100).
# If an entry is invalid the program will alert the user and ask them to resubmit.
# Once the list is complete, the code will find and remove the lowest score in the list.
# From there, the code will calculate the average of the remaining scores.
# Lastly, the program will display the lowest score, the list of remaining scores, the average of the list, and the corresponding letter grade for the average.
#
number_scores = int(input("How many scores would you like to input?: "))
scores = []

print("")
for i in range(number_scores):
    score_input = int(input(f'Enter score #{i + 1}: '))
    while score_input < 0 or score_input > 100:
        print('')
        print('INVLAID Score entered!!!!')
        print('Scores should be between 0 and 100')
        score_input = int(input(f'Enter score #{i + 1} again: '))
    scores.append(score_input)

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
