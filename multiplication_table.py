try:
   num = int(input("Enete Number to multiplay "))
   try:
      x = int(input("Eneter range "))
      for i in range(1,x+1):
         print(num, 'x', i, '=', num*i)
   except:
      print("Input Type Error!")
except:
   print("Input Type Error!")
