
#Define the tax to pay based on the Brazlian tax rule
# untill 1.499,15 - no tax to pay
# from 1.499,16 to 2.246,75 pay 7.5%
# from 2.246,76 to 2.995,70 pay 15.0%
# from 2.995,71 to 3.743,18 pay 22.5%
# above 3.743,19 pay 27.5%

def calculate_tax(payment):
    if payment <= 1499.15:
        percent = 0
        tax_to_pay = payment * percent
    elif payment >= 1499.16 and payment <= 2246.75:
        percent = 0.075
        tax_to_pay = payment * percent
    elif payment >= 2246.76 and payment <= 2995.70:
        percent = 0.15
        tax_to_pay = payment * percent
    elif payment <= 3743.18:
        percent = 0.225
        tax_to_pay = payment * percent
    else:
        percent = 0.275
        tax_to_pay = payment * percent
    return (tax_to_pay, percent)

tax_rate = float(input('Enter your month payment: '))
tax_rate = calculate_tax(tax_rate)
print('Your tax rate is: {1}\nYou will have to pay R$:{0}'.format(*tax_rate))



