# python program to convert decimal into other number systems
try: 
  sum=int(input('enter number '))

  print("the decimal value of  ",sum)
  print(bin(sum),'in binary ')
  print(oct(sum),"octal")
  print(hex(sum),"in hexadecimal")
except Exception as e:
  print("please enter integer number")