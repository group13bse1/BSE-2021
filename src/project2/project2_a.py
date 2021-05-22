# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# function to help with the year
def clean_the_year():
    while True:
        year = input('Enter the year\n')
        if year == '' or year.upper() == 'ALL':
            break
        else:
            try:
                years = int(year)
                if (len(year) < 4) or (years > 1979 and years < 2013):
                    break
                else:
                    print('The year you entered is out of range, try again')
            except:
                print('Invalid format, try again using digits')
    return year
#clean_the_year() end point
# create loop that contiously prompts user to enter (correct) file name
while True:
    fileName = input('Enter file name with \'.txt\':\n')
    fileName = fileName.strip()
    nameLength = len(fileName)
    if nameLength < 5:
        print('File name too short to meet requirements')
    elif fileName.find('.txt', nameLength-4) == -1:
        print('Include \'.txt\' at the end of file name \n')
        # include original file otherwise it will be overwritten
    elif fileName =='measles.txt':
        print('Sorry this name is reserved for a different use')
    else:
        break
#

# To be pythonic we MUST try
try:
    # open file(in write mode) entered by user
    outPutFile = open(fileName, 'w')
    requiredYear = clean_the_year()
    fileobject = open('measles.txt')
    for line in fileobject:
        line = line.strip()
        # make sure every space after year is removed
        lineLength = len(line)
        yearIndex = lineLength - 5
        actualYear = line[yearIndex:]
        actualYear = actualYear.strip()
        if actualYear.startswith(requiredYear):
            outPutFile.write(line)
            outPutFile.write('\n')
        elif (requiredYear == '') or requiredYear.upper() == 'ALL':
            outPutFile.write(line)
            outPutFile.write('\n')


except:
    print('Unable to run the program')