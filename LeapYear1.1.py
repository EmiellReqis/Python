months = ('January','February','March','April','May','June','July','August','September','October','November','December')
days_in_a_month = (31,28,31,30,31,30,31,31,30,31,30,31)
days_in_a_month_leap_year = (31,29,31,30,31,30,31,31,30,31,30,31)


def check_if_year_is_valid():
    while True:
        try:
            year = int(input("Enter year: "))
            if year > 0 and year < 10000:
                return year
            else:
                print("Year must be greater than zero and below 10000") 
        except ValueError:
                print("Provide an integer value")

def check_if_month_is_valid():
    while True:
        try:
            month = int(input("Enter month: "))
            if month > 0 and month <= 12:
                return month
            else:
                print("Enter value in range 1 - 12")
        except ValueError:
                print("Provide an integer value")

def check_if_day_is_valid():    
    while True:           
        try:
            day = int(input("Enter day: "))
            if is_leap_year(year) == False and day > 0 and day <= days_in_a_month[month-1]:
                return day
            elif is_leap_year(year) == True and day > 0 and day <= days_in_a_month_leap_year[month-1]:
                return day
            else:
                print("Enter value in range 1 -",days_in_a_month[month-1])
        except ValueError:
                print("Provide an integer value")

def is_leap_year(year):

    if ((year%4 == 0 and year%100 != 0) or year%400 == 0):
        return True
    else:
        return False

def how_many_days_in_a_month(year,month):
    if is_leap_year(year) == False:
        return days_in_a_month[month - 1]
    else:
        return days_in_a_month_leap_year[month -1]

def which_day_of_the_year(year,month,day):
    i = 1
    day_of_the_year = day
    while i < month:
        day_of_the_year += days_in_a_month[i-1]
        i += 1
    if is_leap_year(year) == True and month > 2:
        day_of_the_year += 1
    return day_of_the_year

if __name__ == "__main__":
    year = check_if_year_is_valid()
    month = check_if_month_is_valid()
    day = check_if_day_is_valid()
    
    if is_leap_year(year) == True:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
    
    print(months[month-1],"have",how_many_days_in_a_month(year,month),"days")
    print("Day of the year:",which_day_of_the_year(year,month,day))
