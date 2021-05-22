# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

try:
    fhand = open('romeo.txt')
except:
    print('unable to open file')

all_words = []
for line in fhand:
    romeo = line.split()
    for word in romeo:
        if word not in all_words:
            all_words.append(word)
all_words.sort()
print(all_words)