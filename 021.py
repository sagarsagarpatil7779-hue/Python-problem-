# Display the power of 2 using anonymous function

ter=12
result=list(map(lambda x:2**x,range(ter)))

print("the total terms are:",ter)
for i in range(ter):
    print("2 raised to power",i,"is",result[i])