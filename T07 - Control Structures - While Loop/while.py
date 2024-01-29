'''
This program continually asks the user to enter a number.
If the user enters “-1”, the program should stop requesting a number.
The program will then calculate the average of the numbers entered, excluding the -1.
'''

# initalising the running total variable, and the running count variable
total = 0
count = 0

# Keep looping until the user enters "-1"
while True:
        try:
            user_num = float(input("Enter a number (to stop enter -1): "))
        except ValueError:
            # If the user does not enter a valid number, display error and loop again
            print("Sorry, invalid input, please enter a number, try again.")
            continue
        else:
            # If the user enters a valid number then add to the running total and count
            if user_num != -1:
                total += user_num
                count += 1
            # if the user has entered "-1" then break the loop
            else:
                break

# Print the average of all the numbers entered excluding the "-1"
print("Average input is: ", total/count)