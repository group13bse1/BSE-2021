#we will initialize a few things here
new_price = None
bal = None
nickel =25 # value is 0.05
dimes = 25 # value is 0.1
quater = 25 # value is 0.25
Ones = 0 # value is 1
fives = 0 # value is 5

#starting point (first display)
print("\n Welcome to the vending machine change maker program")
#function to turn balance into required format.
def dollars_and_cents(money_passed):
    dol_av = int(money_passed /100)
    cent_av = money_passed % 100
    print(f"Payment due is: {dol_av} dollars and {cent_av} cents\n")

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
    #this is the price of the product some one is buying from the v.machine
    input_data = input("Enter the price in form of XX.XX or q to quit..: ")
    if input_data.lower() == "q":
        print("Quited....")
        break
    elif input_data != "q":
        try:

            new_price = float(input_data)
            #turn it into integer make it easy to use
            bal = new_price*100
            #loop; captures customers deposits
            while True:
                if (bal > 0 and (bal % 5 == 0)):
                    choice = input(
                        "\nMenu for deposits:\n"
                        "'n' - deposit a nickel\n"
                        "'d' - deposit a dime\n"
                        "'q' - deposit a quarter\n"
                        "'o' - deposit a one dollar bill\n"
                        "'f' - deposit a five dollar bill\n"
                                   )
                    # if choice != "d" or "n" or "q" or "o" or "f":

                    if (choice == "d"):
                        bal -= 25
                        dimes += 1
                    elif choice == "n":
                        bal -= 5
                        nickel += 1
                    elif choice == "q":
                        bal -= 10
                        quater += 1
                    elif choice == "o":
                        bal -= 100
                        Ones += 1
                    elif choice == "f":
                        bal -= 500
                        fives += 1
                    elif choice == "c":
                        break
                    else:
                        print(f"{choice} is not valid selection")
                    dollars_and_cents(bal)
                    print("indicate your deposit")
                elif new_price < 0:
                    print("illegal entry...")
                elif bal < 0:
                    #at this point, the customer has credit in the machine.
                    #note. the loop should exit the moment this happens
                    #note2. calculate the change based on the available stock
                    change = float(bal * -1) #make it positive for easy calculation

                    balance_in_fives = change // 500
                    change = change % 500
                    if balance_in_fives > fives:
                        change = change + (balance_in_fives - fives)
                        balance_in_fives = fives
                        fives = 0

                    balance_in_ones = change // 100
                    change = change % 100
                    if balance_in_ones > Ones:
                        change = change + (balance_in_ones - Ones)
                        balance_in_ones = Ones
                        Ones = 0
                        # this will be repetitive, maybe a function??


                else:
                    print("Enter correct price foramt")
                    break

        except Exception as e:
            print(e)
            # print("Plizz enter l")
            #remeber to remove this when code is good and ready
            des = input('Pres "N" to enter a new value or "Q" to quit: ')
            if des == "Q":
                break
    else:
        print("Invalid data")
