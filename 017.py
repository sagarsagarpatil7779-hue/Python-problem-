# program to display the fibonacci sequence up to nth term
nt = int(input("Enter number: "))

n1, n2 = 0, 1
count = 0

if nt <= 0:
    print("Please enter a positive number")
elif nt == 1:
    print("Fibonacci sequence:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nt:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
