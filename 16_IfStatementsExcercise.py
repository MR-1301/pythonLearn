# Price of a house is $1M
# If buyer has good credit
#   they need to put down 10%
# Otherwise
#   they need to put down 20%
# Print the down payment

good_credit = False
price = 1000000

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print("$" + str(round(down_payment)))
