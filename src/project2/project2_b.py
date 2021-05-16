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
            print('File not available. Try again')
    return fileHandle
def process_file(fileobject):
    year = input('Please enter the year')
    income = input('Please enter income in this form:'
                   '\n\t 1 \t low income'
                   '\n\t 2 \t lower middle income'
                   '\n\t 3 \t upper middle income'
                   '\n\t 4 \t high income\n')