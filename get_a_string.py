# Simulate a program for a small store
# Use input and output
# Ask users for info on items that were sold

print("Welcome to Diamond's Place! \n\n")
print("Let's proceed to checkout!")
# A series of statements to find out how much of each item has been purchased

candy = int(input("How many candy bars did they buy? "))
drinks = int(input("How many energy drinks did they buy? "))
gas = int(input("How many gallons of gas did they buy? "))

# This section will take each value and multiply it by the current cost per item
candytotal  = candy * 1.50
drinktotal = drinks * 2.50
gastotal = gas * 2.12
subtotal = candytotal + drinktotal + gastotal

# Don't forget sales tax! 7.25% in this example
tax = subtotal * .0725;

#Finally print the itemized receipt

print("\n\nItem     Qnt     Total")
print("-------------------------------")
print("Candy  ", candy, "    $%.2f" % candytotal)
print("Drinks ", drinks, "   $%.2f" % drinktotal)
print("Gas    ", gas, "      $%.2f" % gastotal)
print("-------------------------------")
print("Subtotal      $%.2f" % subtotal)
print("Tax           $%.2f" % tax)
print("Total         $%.2f" % subtotal+tax)
print("\n\nHAVE A GREAT DAY!")
