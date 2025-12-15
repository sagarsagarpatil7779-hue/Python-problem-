#check if year is a leap year or not

year=int(input('enter year'))

# divided by 100 means century year (ending with 00)
# century year  divided by 400 is a leap year 
if (year% 400==0) and (year % 100==0):
    print("{0} is a leap year ".format(year))

# not divided by 100 means not a century year 
# year divided by 4 is a leap year
elif (year%400==0) and (year%100 !=0):
    print("{0} is a leap year ".format(year))
else : # if not divided by both 400 and 4 (not century year)
    print("{0} is a not a leap year".format(year))#year is not a leap year
    