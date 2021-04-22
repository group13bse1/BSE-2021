#we will initialize a few things here
new_price = None
bal = None
nickel =25 # value is 0.05
dimes = 25 # value is 0.1
quater = 25 # value is 0.25
Ones = 0 # value is 1
fives = 0 # value is 5

#create endless loop for entire program
while True:
    print(
        f'\n'
        f'Stock is as follows'
        f'\nNickel {nickel}'
        f'\nDimes  {dimes}'
        f'\nQuater {quater}'
        f'\nOnes   {Ones}'
        f'\nFives  {fives}'
    )
    input_data = input("Enter the price in form of XX.XX or q to quit..: ")
    if input_data == "q":
        print("Quited....")
        break
    elif input_data != "q":
        try:

            new_price = float(input_data)
            #turn it into integer make it easy to use
            bal = int(new_price*100)

            #will add the function updating stock for

        except Exception as e:
            print(e)
            # print("Plizz enter l")
            des = input('Pres "N" to enter a new value or "Q" to quit: ')
            if des == "Q":
                break
    else:
        print("Invalid data")
