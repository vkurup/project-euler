#!/usr/bin/env python2

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a
#   century unless it is divisible by 400. 
# How many Sundays fell on the first of the month during the twentieth
#   century (1 Jan 1901 to 31 Dec 2000)? 

def day_of_week(year, month, day):
    """Return integer day of week (0 = Sunday) for year/month/day provided"""
    return (count_days(year, month, day) + 1) % 7

def count_days(year, month, day):
    """Count number of days since 1900, 01, 01"""
    # years
    days = (year - 1900) * 365

    # months
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    days += sum(months[:month])

    # days
    days += (day - 1)

    # account for leap years
    if month > 2: # make sure to account for this year
        year += 1
    days += len([y for y in range(1900,year) 
                 if y%4 == 0 
                 if (y%100 != 0) or (y%400 == 0)])
    return days

#print day_of_week(2012,4,28)
print [day_of_week(y,m,1) for y in range(1901,2001)
       for m in range(1,13)].count(0)
 
