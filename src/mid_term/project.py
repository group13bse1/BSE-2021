# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# program functions
def CalculateGallons(a, b):
    a = float(a)
    b = float(b)
    gallonValue = a - b
    if gallonValue < 0:
        gallonValue = (gallonValue * -1) + 1000000000
    calculatedGallonValue = float(gallonValue / 10)
    return calculatedGallonValue

def billCustomer(oldChoice, gallons):
    choice = oldChoice.lower()
    if choice == 'r':
        billPrice = 5 + (gallons * 0.005)
        return billPrice
        #print('choice is r')
    elif choice == 'c':
        if gallons > 4000000:
            extraCharge = (gallons - 4000000) * 0.00025
            billPrice = extraCharge + 1000
        else:
            billPrice = 1000
        return billPrice
        #print('choice is c')
    elif choice == 'i':
        if gallons <= 4000000:
            billCharge = 1000
        elif gallons <= 10000000:
            billCharge = 2000
        else:
            extraCharge = (gallons - 10000000) * 0.00025
            billCharge = extraCharge + 2000
        #print('choice is i')
    return billCharge
    #print('bill the customer function')

def fillWithZeros(a):
    turnToString = str(a)
    completeFill = turnToString.zfill(9)
    return completeFill
while True:
    customerCode = input("Enter customer code")
    if(customerCode.lower() == 'r') or (customerCode.lower() == 'c') or (customerCode.lower() == 'i'):
        print('run this')
        begMeterReading = input('Enter beginning meter reading:')
        endMeterReading = input('Enter ending meter reading:\n')
        caculatedGallonsReading = CalculateGallons(endMeterReading, begMeterReading)
        amountBilled = billCustomer(customerCode, caculatedGallonsReading)
        # formating figures for display
        begMeterReading = fillWithZeros(begMeterReading)
        endMeterReading = fillWithZeros(endMeterReading)
        formatedGallons = fillWithZeros(caculatedGallonsReading)
        formatedAmountBilled = "${:,.2f}".format(amountBilled)
        print(
            f'\n'
            f'Customer code: {customerCode}'
            f'\nBeginning meter reading: {begMeterReading} '
            f'\nEnding meter reading: {endMeterReading}  '
            f'\nGallons of water used: {formatedGallons}'
            f'\nAmount billed: {formatedAmountBilled}  \n'
        )

    else:

        break
