# Swap without using temporary variable
x = 10
y = 5
x = x + y
y = x - y
x = x - y
print ( "x = " + str(x) + " y=" + str(y))

# Swap using temporary varaible

temp = x
x = y
y = temp
print ( "x = " + str(x) + " y=" + str(y))

#Using Bitwise XOR to swap 

x ^= y 
y ^= x  
x ^= y 
print ( "x = " + str(x) + " y=" + str(y))

# Python Swap 

x,y = y,x 
print ( "x = " + str(x) + " y=" + str(y))
