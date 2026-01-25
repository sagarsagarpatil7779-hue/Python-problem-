# To find a L.C.M of two number

def my_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if ((greater%x==0) and(greater%y==0)):
            lcm=greater
            break
        greater +=1
    return lcm
num1=3
num2=3
print("the L.C.M is",my_lcm(num1,num2))
    