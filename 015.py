# python program to find factorial of a number provided by the user.
try:
   num=int(input("enter any number to find factorial"))

   factorial=1


   if num<0:
      print("factrial does not exist for negative numbers")
   elif num==0:
     print("he factorial of 0 is 1")
   else:
     for i in range(1,num+1):
        factorial=factorial*i
   print("the factorial pf",num,"is",factorial)
except Exception as e:
   print("please enter integer value")