# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMIYALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# question
# Use find and string slicing to extract the portion
# of the string after the colon character and then use the float function to convert the
# extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475 '
startingpoint = str.find(':')
# get the desired part
desiredString = str[startingpoint +1 : ]
# strip the blanks from it
cleanString = desiredString.strip()
#convert it to float
floatValue = float(cleanString)
print(floatValue)