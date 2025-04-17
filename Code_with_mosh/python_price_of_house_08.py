# price of a house is $1M 
# if buyer has good credit
#     they need to put down 10%
# Otherwise
#     they need to put down 20%
# print the down payment

price = 1000000

# if he has a good credit score
score = input("Do you have a good creidt score ? (yes/no): ").lower()
if score == "yes":
    credit = True
else: 
    credit = False

def credit_score(has_good_credit):
    if has_good_credit:
        down_payment = 0.1 * price
    else:
        down_payment = 0.2 * price
    print(f"Down payment: ${down_payment}")

credit_score(has_good_credit = credit)

