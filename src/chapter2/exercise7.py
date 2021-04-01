money_entered1 = input("Enter an amount to make change for \n")
money_entered = float(money_entered1)
print("Your change is...\n \n")

twenties = 20
tens = 10
fives = 5
ones = 1
quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01

no_of_20s = int(money_entered / twenties)
money_left = (money_entered % twenties)

no_of_10s = int(money_left / tens)
money_left = money_left % tens

no_of_5s = int(money_left / fives)
money_left = money_left % fives

no_of_ones = int(money_left / ones)
money_left = money_left % ones

no_of_quarters = int(money_left / quarters)
money_left = money_left % quarters

no_of_dimes = int(money_left / dimes)
money_left = money_left % dimes

no_of_nickels= int(money_left / nickels)
money_left= money_left % nickels

no_of_pennies= int(money_left / pennies)
money_left= money_left % pennies

print(no_of_20s, 'TWENTIES \n')
print(no_of_10s, 'TENS \n')
print(no_of_5s, 'FIVES \n')
print(no_of_ones, 'ONES \n')
print(no_of_quarters, 'QUARTERS \n')
print(no_of_dimes, 'DIMES \n')
print(no_of_nickels, 'NICKELS \n')
print(no_of_pennies, 'PENNIES \n')