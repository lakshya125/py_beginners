#Python programme to print fibonacci series
n = int(input("Enter number of terms to be printed: "))
first = 0
second = 1
print(first)
print(second)
for x in range(0, n-2 ) :
  third = first + second
  first , second =second,third
  print(third)
