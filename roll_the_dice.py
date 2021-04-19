import random
MINIMUM = 1
MAXIMUM = 6

roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print("Rolling the dices...")
    print(f"Your number is {random.randint(MINIMUM, MAXIMUM)}")
    roll_again = input("Roll the dices again? yes(y)/no(n)")
