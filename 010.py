#check if a number is a odd or even

#check if a number is a odd or even

num=int(input("enter a number"))

if num<0:
    print("enter positive number")
elif num%2==0:
    print("even number {}".format(num))
else:
    print(f"{num} it is odd number")



