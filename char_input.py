import datetime

name = input("Please enter your name: ")
age = input("Please enter your age: ")

current_year = datetime.date.today().year

hundredth_year = current_year - int(age) + 100

print("You will turn 100 in the year", hundredth_year)
