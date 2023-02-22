#ex1
import datetime
"""
1.Write a Python program to subtract five days from current date.
"""
today = datetime.datetime.now()
fivedaysago = today.day - 5
answer = datetime.date(today.year, today.month, fivedaysago)
print(answer)


#ex2
import datetime
"""
2.Write a Python program to print yesterday, today, tomorrow.
"""
today1 = datetime.datetime.today()
print(today1)

tomorrow = today1.day + 1 
tomorrow_ans = datetime.datetime(today.year, today.month, tomorrow)
print(tomorrow_ans)

yesterday = today1.day - 1
yesterday_ans = datetime.datetime(today.year, today.month, yesterday)
print(yesterday_ans)

#ex3
import datetime
"""
3.Write a Python program to drop microseconds from datetime.
"""
day1 = datetime.datetime.today().replace(microsecond=0)
print(day1)

#ex4
import datetime as dt
"""
4.Write a Python program to calculate two date difference in seconds.
"""
date1 = dt.datetime.today()
date2 = dt.datetime(2022,2,21)
print((date1-date2).total_seconds())
