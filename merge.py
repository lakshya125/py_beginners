# Lets merge two strings together
# Ask for the users's hometown and state
# Display it in this format, city, state

# Ask user for their hometown
town = input("What city are you form? ")

# Ask the user for their state
state = input("What state are you from? ")

# Make a comma-seperated variable for city, state
fullLocation = town + ', ' + state

print("So you are from ", fullLocation)