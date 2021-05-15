# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

fileHandle = input('Enter file name \n')
# the pythonic way, use try
try:
    # open input file and put it in handle
    fhandle = open(fileHandle)
    #fhandle = open('mbox-short.txt')
    #inntiate the variables to use in loop
    numberoflines = 0
    totaloffloatingpoints = 0
    for iteration in fhandle:
        iteration = iteration.rstrip()
        #use find to find the required values
        #note. when nothing is found, python returns -1
        #print(iteration)
        if iteration.find('X-DSPAM-Confidence') != -1:
            indexposition = (iteration.find(':')) + 1
            #takes us to the position after ":"
            floatingnumber = iteration[indexposition: ]
            #will slice the string from the position above to the end
            #print(type(floatingnumber))
            floatingnumber = floatingnumber.strip()
            #print(floatingnumber)
            floatingnumber = float(floatingnumber)
            #print(type(floatingnumber))
            totaloffloatingpoints = totaloffloatingpoints + floatingnumber
            numberoflines += 1
    #print(totaloffloatingpoints)
    averagespamconfidence = totaloffloatingpoints / numberoflines
    print('The average of spam confidence is: \n '
          f'\t{format(averagespamconfidence,".4f")}')

except:
    #print('something is wrong')
    print('The file '
          f'\t {fileHandle} does not exist in directory')