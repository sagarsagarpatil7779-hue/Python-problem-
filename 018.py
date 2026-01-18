# program ti check if the number is an Armstrong number or not

num_1=int(input("enter a number :"))

# intialize sum_1
sum_1=0

# find the sum of the cube of each digit
tem=num_1
while tem>0:
    digit = tem%10
    sum_1 += digit **3
    tem //=10
if num_1==sum_1:
   print(num_1,"is a Armstrong number")
else:
    print(num_1,"is not a Armstrong number")
