"""price of a house is $1M
If buyer has good credit
then need to put down 10%
otherwise
they need to put down 20%
print the down payment"""

price=100000
has_good_credit=False
if has_good_credit:
    down_payment = 0.1 * price
    print(f'down_payment:${down_payment}')
else:
    down_payment=0.2*price
    print(f'down_payment:${down_payment}')
