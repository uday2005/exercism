def leap_year1(year):
    if year%4 == 0 and year % 100 != 0:
        return True
    elif year%100 == 0 and year%400 == 0:
        return True
    else:
        return False


# So here one thing we can improve in boolean expression is that elif statement if a number 
# is divided by 400 then it must be divided by 100 so we dont need to write about it


def leap_year2(year):
    if year%4  == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    else:
        return False


# we can do it more small likew in one line

def leap_year3 (year):
    return year%4 == 0 and year %100 != 0 or year%400 == 0

