# sum of  natural number upto num
num=int(input("ente a number"))

if num<0:
    print('please enter positive number')
else:
    sum=0
    # use while loop to  iterate untile Zero
    while(num>0):
        sum +=num
        num -=1
    print("the sum is",sum)