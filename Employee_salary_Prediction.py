hours_str=input("Enter hours: ")
rate_str=input("Enter rate: ")
try:
    hours=float(hours_str)
    rate=float(rate_str)
except:
    print("please enter the number values")
    quit()
if (hours<=40):
    pay=hours*rate
else:
    ordinary_pay = 40*rate
    overtime_pay = (hours-40)*(rate*1.5)
    pay=ordinary_pay+overtime_pay
print("pay :",pay)