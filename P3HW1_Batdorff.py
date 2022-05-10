# CTI-110
# P3HW1 - Debugging
# John Batdorff 
# 3/22/2022
#
# This program debugs and finishes partially started program that takes a students number grade and determines the corresponding letter grade.
# No mathematical calculation are necessary, but uses if else statements to accurately determine the letter grade.
# Lastly, the program will output the number grade and the letter grade back to the user.
# 
def main():
    score = int(input('Enter grade: '))
    if score >= 90:
        print('Your grade is: A')
    else:
        if score >= 80:
            print('Your grade is: B')
        else:
            if score >= 70:
                print('Your grade is: C')
            else:
                if score >= 60:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F')

main()
