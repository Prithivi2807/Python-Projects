age = input("what is your current age ? ")

# 90 years old how many months, weeks, days are there ? for them selves ?

remaining_age = 90 - int(age)

remaining_month = remaining_age * 12
remaining_weeks = remaining_age * 56
remaining_days = remaining_age * 365

print(f"if you're age is {age} you only have {remaining_month} months, {remaining_weeks} weeks, {remaining_days} days ")