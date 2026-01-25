
#To find the factor of a number

def print_factors(x):
    print("the factors of ",x,"are:")
    for i in range(1,x+1):
        if x % i ==0:
            print(i)
num=320
print_factors(num)



x=24
for i in range(1,x+1):
    if x%i==0:
     print(i)

