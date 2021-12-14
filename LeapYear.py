while True:
    print("To check if it's a leap year enter a year and 0 in month and day")
    print("To check how many days is in month, enter a year and month and 0 in day")
    print("To check which day of the year it is, enter all values above 0 and in the correct range")

    monthsTO = (1,3,5,7,8,10,12)
    while True:
        try:
            year = int(input("Enter year: "))
            if year <= 0 or year > 9999:
                print("Year must be greater than zero and below 10000")
            else:
                break
        except ValueError:
            print("Provide an integer value")
            continue
    while True:
        try:
            month = int(input("Enter month: "))
            if month < 0 or month > 12:
                print("Enter value in range 0 - 12")
            else:
                break
        except ValueError:
            print("Provide an integer value")
            continue
    
    if (month in monthsTO):
        while True:
            try:
                day = int(input("Enter day: "))
                if day < 0 or day > 31:
                    print("Enter value in range 0 - 31")
                else:
                    break
            except ValueError:
                print("Provide an integer value")
                continue
    elif (month == 2):
        if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
            while True:
                try:
                    day = int(input("Enter day: "))
                    if day < 0 or day > 29:
                        print("Enter value in range 0 - 29")
                    else:
                        break
                except ValueError:
                    print("Provide an integer value")
                    continue
        else:
            while True:
                try:
                    day = int(input("Enter day: "))
                    if day < 0 or day > 28:
                        print("Enter value in range 0 - 28")
                    else:
                        break
                except ValueError:
                    print("Provide an integer value")
                    continue
    else:
        while True:
            try:
                day = int(input("Enter day: "))
                if day < 0 or day > 30:
                    print("Enter value in range 0 - 30")
                else:
                    break
            except ValueError:
                print("Provide an integer value")
                continue 
    
    

    

    def is_leap_year():

        if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
            print("It's a Leap year") 
        else:
            print("It's not a Leap year")

    def how_many_days_in_a_month():
        if month in monthsTO:
            print("This month has 31 days")
        elif (month == 2):
            if((year%4 == 0 and year%100 != 0) or year%400 == 0):
                print("This month has 29 days")
            else:
                print("This month has 28 days")
        else:
            print("This month has 30 days")

    def which_day_of_the_year():
        if((year%4 == 0 and year%100 != 0) or year%400 == 0):
            i = 1
            that_day = 0
            while i < month:

                if i in monthsTO:
                    that_day += 31
                elif i == 2:
                    that_day += 29
                else:
                    that_day +=30
                i+=1
        else:
            i = 1
            that_day = 0
            while i < month:
                if i in monthsTO:
                    that_day += 31
                elif i == 2:
                    that_day += 28
                else:
                    that_day +=30
                i+=1
        that_day += day
        print("it is ", that_day, "day of a year" )

    if (year > 0 and month == 0 and day == 0):
        is_leap_year()
    elif(year > 0 and month != 0 and day == 0):
        how_many_days_in_a_month()
    elif(year > 0 and month != 0 and day != 0):
        which_day_of_the_year()
    else:
        print("Enter corect date, year can't be below 1, month must be in range 0-12, and day must be in range 0-31")
        
    
    check = input("End the program? Y/N: ")
    if check.upper() == "N":
        continue
    break