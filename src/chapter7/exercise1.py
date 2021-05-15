# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

fileHandle = input('Enter file name')
try:
    fhandle = open(fileHandle)
    for iteration in fhandle:
        iteration = iteration.rstrip()
        iteration = iteration.upper()
        print(iteration)
except:
    print('The file '
          f'\t {fileHandle} does not exist in directory')