# a program check if a number is prime or not
try:
    num=int(input("enter a number"))
    Flag=False

    if num==0 or num==1:
        print(num,"is not a prime number")
    elif num>1:
        for i in range(2,num):
           if (num%i)==0:
               Flag=True
               break
    if Flag:
        print(num, "is not a prime number")
    else:
        print(num,"is a prime number")
except ValueError:
    print("please enter integer value")