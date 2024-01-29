# Get User's age
#age = 45        # Test Data
age = int(input("Enter your age : "))

if age > 100:
    print("Sorry, you're dead")
elif age >= 65:
    print("Enjoy your retirement")
elif age >= 40:
    print("You're over the hill")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 13:
    print("Age is but a number")
else:
    print("You qualify for the kiddie discount")

