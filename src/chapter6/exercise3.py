# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# encapsulate the code given into a function called count

# creating the function count
def count(word, letter):
    countingNumber = 0
    for loopingLetter in word:
        if loopingLetter == letter:
            countingNumber = countingNumber + 1
    print(countingNumber)

# main program
word = input('enter word \n')
letter = input('enter the letter to be counted \n')
# using/calling the function count
count(word, letter)