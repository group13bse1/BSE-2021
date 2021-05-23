# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

# modified the 'mbox-short.txt' file by shortening the first line in 'exercise2.txt'
fhand = open('exercise2.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    #if len(words) == 0 : continue
    # the line above was problematic
    if len(words) < 3: continue
    if words[0] != 'From': continue
    print(words[2])

