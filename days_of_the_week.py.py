def is_year_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False

#
# Your code from LAB 4.3.1.6.
#

# def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#

def days_in_month(year, month):
    if (month == 1):
        return 31
    elif (month == 2) and (is_year_leap(year) == False): 
        return 28 
    elif (month == 2) and (is_year_leap(year) == True):
        return 29
    elif (month == 3):
        return 31
    elif (month == 4):
        return 30
    elif (month == 5):
        return 31
    elif (month == 6):
        return 30
    elif (month == 7):
        return 31
    elif (month == 11): 
        return 30
    elif (month == 10):
        return 31
    elif (month == 9):
        return 30
    elif (month == 10):
        return 31
    elif (month == 8):
        return 31
    elif (month == 12):
        return 31
    else:
        return None

def day_of_year(year, month, day):
#
# Write your new code here.
#
    t = [ 0, 3, 2, 5, 0, 3,
         5, 1, 4, 6, 2, 4 ]
    year -= month < 3
    day =  (( year + int(year / 4) - int(year / 100)
             + int(year / 400) + t[month - 1] + day) % 7) 
    if day == 0:
        return "Sunday"
    elif day == 1: 
        return "Monday" 
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else: 
        return None
print(day_of_year(2022, 2, 9))
