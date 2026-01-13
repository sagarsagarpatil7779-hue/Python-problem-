#python to display multiplication table

try:
    num=int(input("enter number for multiplication"))
    
    if num<0 :
        print("sorry you enter negative  number")
    elif num==0:
        print("enter postive number")
    else:
        for i in range(1,11):
         print(f"{num}x{i}={num*i}")
except ValueError as Exception:
   print("please enter integer value")