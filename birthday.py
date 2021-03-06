"""
birthday.py
Author: kyDoleuc04
Credit: Mr. Dennison
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
print("Hi",name+",","what was the name of the month you were born in? ")
birthmonth = input()
print("And what year were you born in,",name+"? ")
birthyear = float(input())
birthday = float(input("And the day? "))
month = month_name[todaymonth]

if birthmonth=="October" and int(birthday)==31:
    print("You were born on Halloween!")
elif birthmonth==month and birthday==int(todaydate):
    print("Happy birthday!")
else: 
    if birthmonth=="December" or birthmonth=="January" or birthmonth=="February":
        season="winter"
    elif birthmonth=="March" or birthmonth=="April" or birthmonth=="May":
        season="spring"
    elif  birthmonth=="June" or birthmonth=="July" or birthmonth=="August":
        season="summer"
    elif birthmonth=="September" or birthmonth=="October" or birthmonth=="November":
        season="fall"
    if int(birthyear)>=2000:
        era="two thousands"
    elif 1990<=int(birthyear)<2000:
        era="nineties"
    elif 1980<=int(birthyear)<1990:
        era="eighties"
    elif int(birthyear)<1980:
        era="Stone Age"
    print(name+", you are a",season,"baby of the",era+".")