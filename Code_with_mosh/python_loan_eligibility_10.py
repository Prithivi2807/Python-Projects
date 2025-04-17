# if applicant has high income OR good credit 
#     Eligible for loan 

# if applicant has good credit AND doesn't have criminal record
# AND: both
# OR: at least one 
# NOT:

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("you are not elgible for loan")
