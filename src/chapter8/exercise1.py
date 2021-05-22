# MATSIKO BRUNO 2020/BSE/165/PS
# DAVID NYAMUTALE 2020/BSE/057/PS
# MAWANDA DENNIS 2020/BSE/155/PS
# AKANDWANAHO NICKSON 2020/BSE/006/PS

def chop(list_name):
    del list_name[-1]
    del list_name[0]
def middle(list_name):
    return list_name[1:-1]


my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(middle(my_list))
#print(chop(my_list))
chop(my_list)
print(my_list)
