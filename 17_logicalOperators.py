# note that all operators must me in lowercase

# if applicant has high income and good credit then he/she is eligible for loan
# logical "and" operator
# all of them needs to be true for an entire expression to be evaluated as true
good_credit = True
high_income = True
if good_credit and high_income:
    print("Eligible for Loan!!")
else:
    print("Not Eligible For Loan!!")

# if applicant has high income or good credit then he/she is eligible for loan
# Logical "or" operator
# at least one of them needs to be true for an entire expression to be evaluated as true
good_credit = True
high_income = False
if good_credit or high_income:
    print("Eligible for Loan!!")
else:
    print("Not Eligible For Loan!!")

# Not operator converts any value given to it as opposite to already present
isOK = True
print(not isOK)

# # if applicant has high income and no Criminal Record then he/she is eligible for loan
high_income = True
criminal_record = False

if high_income and (not criminal_record):
    print("Eligible for Loan!!")
else:
    print("Not Eligible For Loan!!")

# always keep a habit of writing () where there is multiple operators working side by side
