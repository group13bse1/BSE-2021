# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

my_list = []
while True:
    number = input('Enter a number: \n')
    try:
        value = float(number)
        my_list.append(value)
    except:
        break
maximum_number = max(my_list)
minimun_number = min(my_list)

print(f'The maximum number is:\t {maximum_number} '
      f'\nand '
      f'\nThe minimum number is:\t{minimun_number}')