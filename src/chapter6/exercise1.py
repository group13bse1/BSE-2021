# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# while loop that starts at the last character in a string and works it way backwords to the start of string.
# print each letter on seperate line except back words

stringname = input('enter the string to be reversed')
stringlength = len(stringname)
while ( stringlength > 0 ):
    print(stringname[stringlength - 1])
    stringlength = stringlength - 1