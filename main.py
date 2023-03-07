# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_last = 90 - int(age)
months_last = years_last * 12
weeks_last = years_last * 52
days_last = years_last * 365

print(f"You have {days_last} days, {weeks_last} weeks, and {months_last} months left.")
