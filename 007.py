# check if a number is positive or nagative 
try:
    num_1=int(input ("enter a number i will tell you positive or negative "))

    if num_1>0:
        print(f"{num_1} is a positive ")
    elif num_1==0:
        print(f"{num_1} is a negative ")
    elif num_1<0:
        print(f"{num_1} is  a constant")
    else :
        print("invalid")
except ValueError:
    print("please enter integer value")