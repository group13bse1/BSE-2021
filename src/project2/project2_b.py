# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMITALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

def open_file():
    while True:
        #fileName = input('Enter file name \n')
        try:
            #fileHandle = open(fileName)
            fileHandle = open('measles.txt')
            break
        except:
            print('File not available. Try again with correct file name')
    return fileHandle
# end of open file function
def process_file(fileObject):
    while True:
        yearEnterd = input('Please enter the year\n')
        if len(yearEnterd) == 4:
            try:
                # make sure the year entered is a number
                yearchecker = int(yearEnterd)
                if yearchecker > 1979 and yearchecker < 2013:
                    break
                else:
                    print('year is not in range')
            except:
                print('Invalid, year should be digits')
        else:
            print('year should have 4 digits')



    #yearEnterd = '2000'
    while True:
        incomeSelected = input('Please select income:'
                               '\n\t 1 \t Low income'
                               '\n\t 2 \t Lower middle income'
                               '\n\t 3 \t Upper middle income'
                               '\n\t 4 \t High income\n')
        if incomeSelected == '1':
            incomeIs = 'WB_LI'
            display_name = 'Low income'
            break
        elif incomeSelected == '2':
            incomeIs = 'WB_LMI'
            display_name = 'Lower middle income income'
            break
        elif incomeSelected == '3':
            incomeIs = 'WB_UMI'
            display_name = 'Upper middle income'
            break
        elif incomeSelected == '4':
            incomeIs = 'WB_HI'
            display_name = 'High income'
            break
        else:
            print('You entered false value, try again')
    counter = 0
    vaccine_total = 0
    lowestPercent = None
    highestPercent = None
    contrywithhiest = None
    contrywithlowest = None
    for line in fileObject:
        if (line.find(incomeIs) != -1) and (line.find(yearEnterd) != -1):
            country = line[:50]
            country = country.strip()
            percent_of_vac = line[58:61]
            percent_of_vac = percent_of_vac.strip()
            percent_of_vac = int(percent_of_vac)
            # start point......getting the highest and lowest values
            if (lowestPercent is None) or (highestPercent is None):
                lowestPercent = percent_of_vac
                highestPercent = percent_of_vac
                contrywithhiest = country
                contrywithlowest = country
            elif lowestPercent > percent_of_vac:
                contrywithlowest = country
                lowestPercent = percent_of_vac
            elif highestPercent < percent_of_vac:
                contrywithhiest = country
                highestPercent = percent_of_vac
            # end point......getting the highest and lowest values
            counter = counter + 1
            vaccine_total = vaccine_total + percent_of_vac
    # for loop end point
    average_vaccine = vaccine_total / counter
    print(f'For:'
          f'\n\tThe year:\t {yearEnterd}'
          f'\n\tIncome :\t {display_name}'
          f'\n\n\tCount :\t {counter}'
          f'\n\tAverage percentage:{average_vaccine}'
          f'\n\tHighest percentage:{highestPercent}\tCountry: {contrywithhiest}'
          f'\n\tLowest percentage:{lowestPercent}\tCountry: {contrywithlowest}')




selectedFile = open_file()
process_file(selectedFile)