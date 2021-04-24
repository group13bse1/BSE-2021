#MATSIKO BRUNO 2020/BSE/165/PS
#DAVID NYAMIYALE 2020/BSE/057/PS
#MAWANDA DENNIS 2020/BSE/155/PS
#AKANDWANAHO NICKSON 2020/BSE/006/PS

#we will initialize a few things here
new_price = None
bal = None
nickel =25 # value is 0.05
dimes = 25 # value is 0.1
quater = 25 # value is 0.25
Ones = 0 # value is 1
fives = 0 # value is 5
change_catcher = 0

#starting point (first display)
print("\n Welcome to the vending machine change maker program \n Change maker initialized ")
#function to turn balance into required format.
def dollars_and_cents(money_passed):
    dol_av = int(money_passed /100)
    cent_av = int(money_passed % 100)
    if dol_av == 0:
        print(f"Payment due is: {cent_av} cents\n")
    else:
        print(f"Payment due is: {dol_av} dollars and {cent_av} cents\n")

while True:
    print(
        f'\n'
        f'Stock is as follows'
        f'\n{nickel} Nickel '
        f'\n{dimes} Dimes  '
        f'\n{quater} Quarters '
        f'\n{Ones} Ones   '
        f'\n{fives} Fives  '
    )
    #this is the price of the product some one is buying from the v.machine
    input_data = input("Enter the price in form of XX.XX or q to quit..: ")
    if input_data.lower() == "q":
        print("Quited....")
        break
    elif input_data != "q":
        try:

            new_price = float(input_data)
            #turn it into integer & make it easy to use
            bal = new_price*100
            print(
                "\nMenu for deposits:\n"
                "'n' - deposit a nickel\n"
                "'d' - deposit a dime\n"
                "'q' - deposit a quarter\n"
                "'o' - deposit a one dollar bill\n"
                "'f' - deposit a five dollar bill\n"
                )
            #loop; captures customers deposits
            while True:
                if (bal > 0 and (bal % 5 == 0)):
                    dollars_and_cents(bal)
                    choice = input("Indicate your deposit:")# if choice != "d" or "n" or "q" or "o" or "f":

                    if (choice.lower() == "d"):
                        bal -= 10
                        dimes += 1
                        change_catcher += 10
                    elif choice.lower() == "n":
                        bal -= 5
                        nickel += 1
                        change_catcher += 5
                    elif choice.lower() == "q":
                        bal -= 25
                        quater += 1
                        change_catcher += 25
                    elif choice.lower() == "o":
                        bal -= 100
                        Ones += 1
                        change_catcher += 100
                    elif choice.lower() == "f":
                        bal -= 500
                        fives += 1
                        change_catcher += 500
                    elif choice.lower() == "c":
                        bal_changer = change_catcher
                        #oth = (new_price*100) - bal
                        #print(change_catcher)
                        #print(oth)
                        break
                    else:
                        print(f"Illegal selection : {choice} ")

                elif new_price < 0:
                    print("illegal entry...")
                elif bal < 0:
                    bal_changer = bal * -1
                    break
                else:
                    print("Illegal price: Must be a non-negative multiple of 5")
                    bal_changer = 0
                    break
            # from here we calculate customer change.
            if bal_changer != 0:
                print('Please take the change below')
                # calculating ones
                customer_ones = bal_changer // 100
                bal_changer = bal_changer % 100
                if customer_ones > Ones:
                    bal_changer = bal_changer + (customer_ones - Ones)*100
                    customer_ones = Ones
                    Ones = 0
                else:
                    Ones = Ones - customer_ones
                if customer_ones != 0:
                    print(f" {int(customer_ones)} Ones\n")
                #calculating quater
                customer_quater = bal_changer // 25
                bal_changer = bal_changer % 25
                if customer_quater > quater:
                    bal_changer = bal_changer + (customer_quater - quater)*25
                    customer_quater == quater
                    quater = 0
                else:
                    quater = int(quater - customer_quater)
                if customer_quater != 0:
                    print(f" {int(customer_quater)} Quarters\n")
                # calculating dimes
                customer_dimes = bal_changer // 10
                bal_changer = bal_changer % 10
                if customer_dimes > dimes:
                    bal_changer = bal_changer + (customer_dimes - dimes)*10
                    customer_quater == quater
                    dimes = 0
                else:
                    dimes = int(dimes - customer_dimes)
                if customer_dimes != 0:
                    print(f" {int(customer_dimes)} Dimes\n")
                # calculating nickel
                customer_nickel = bal_changer // 5
                bal_changer = bal_changer % 5
                if customer_nickel > nickel:
                    bal_changer = bal_changer + (customer_nickel - nickel)*5
                    customer_nickel == nickel
                    nickel = 0
                else:
                    nickel = int(nickel - customer_nickel)
                if customer_nickel != 0:
                    print(f" {int(customer_nickel)} Nickels\n")
                if bal_changer != 0:
                    print('Machine is out of change.\n See the store manager for remaining refund.\n ')
                    dollars_and_cents(bal_changer)

        except Exception as e:
            print(e)
            # print("Plizz enter l")
            # Remember to remove this when code is good and ready
            des = input('Pres "N" to enter a new value or "Q" to quit: ')
            if des.upper() == "Q":
                break
    else:
        print("Invalid data")
