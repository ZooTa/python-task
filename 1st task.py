from datetime import datetime
date = datetime.date(datetime.now())
print("please enter your birhday date")
day = int(input("please enter the day "))
month = int(input("please enter the month "))
year = int(input("please enter the year "))
age = date.year - year

if day > 0 and month > 0 and year > 0 :
    if year <= 2020:
        if month <= 12:
            if day <= 31:
                print("valid data")
                if day == date.day and month == date.month :
                    print("happy birthday gamed \n you are " + str(age) +" years old now")
                
            else:
                print("invalid day") 
        else:
            print("invalid month")    
    
    else:
        print("invalid data")    

else:
    print("invalid date")



