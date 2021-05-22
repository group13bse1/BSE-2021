# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

try:
    fhand = open('mbox-short.txt')
    count = 0
    for line in fhand:
        words = line.split()
        if (len(words) == 0) or (words[0] != 'From'):
            continue
        count += 1
        print(words[1])
    print(f'There were {count} lines in the file with From as the first word')
except:
    print('unable to open file')