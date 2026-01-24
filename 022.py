# python program to find number diviible by another number 

# first take a list 

my_list=[23,34,56,39,102,235,346]

#using anonymous function to filter
res=list(filter(lambda x:(x%13==0),my_list))
print(res)

