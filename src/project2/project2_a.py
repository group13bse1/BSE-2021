# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# create loop that contiously prompts user to enter the correct file
while True:
    fileName = input('Enter the name of file with .txt extension to save into: \n')
    fileName = fileName.strip()
    nameLength = len(fileName)
    if nameLength < 4:
        print('please include the extension .txt at the end of file name \n')
    elif fileName.find('.txt', nameLength-4) == -1:
        print('please include the extension .txt at the end of file name \n')
    else:
        break
#

# To be pythonic MUST try
try:
    # Read the measles file
    outPutFile = open(fileName, 'w')
    requiredYear = input('Enter the year: \n')
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