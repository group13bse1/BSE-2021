# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS
def open_file():
    while True:
        fileName = input('Enter file name \n')
        try:
            fileHandle = open(fileName)
            break
        except:
            print('File not available. Try again with correct file name')
    return fileHandle
def process_file(fileObject):
    yearEnterd = input('Please enter the year\n')
    while True:
        incomeSelected = input('Please select income:'
                               '\n\t 1 \t low income'
                               '\n\t 2 \t lower middle income'
                               '\n\t 3 \t upper middle income'
                               '\n\t 4 \t high income\n')
        if incomeSelected == '1':
            incomeIs = 'WB_LI'
            break
        elif incomeSelected == '2':
            incomeIs = 'WB_LMI'
            break
        elif incomeSelected == '3':
            incomeIs = 'WB_UMI'
            break
        elif incomeSelected == '4':
            incomeIs = 'WB_HI'
            break
        else:
            print('You entered false value, try again')
    counter = 0
    total = 0
    country = None
    for line in fileObject:
        if (line.find(incomeIs) != -1) and (line.find(yearEnterd) != -1):
            print(line.strip())


selectedFile = open_file()
process_file(selectedFile)