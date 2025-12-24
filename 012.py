# finding a largest number among three numbers 

a =int(input("enter first number"))
b = int(input("enter second number "))
c = int(input("enter third number "))

if a>b and a>c:
    print(f"{a} is largest number")
elif b>a and b>c:
    print(f"{b} is largest number")
else:
    print(f"{c} is a largest number")