#used the same loop to capture the inputs as exercise1
#list of group members
    #MATSIKO BRUNO 2020/BSE/165/PS
    #DAVID NYAMUTALE 2020/BSE/057/PS
    #MAWANDA DENNIS 2020/BSE/155/PS
    #AKANDWANAHO NICKSON 2020/BSE/006/PS
# strt with an empty list
list_of_items_to_capture = []
#create a loop for capturing values
random_number = 1
while random_number == 1:
    inputedValue = input('enter  values, else enter done\n')
    if len(inputedValue) == 0:
        print('bad data')
    elif inputedValue.lower() == "done":
        random_number = 2
    else:
        try:
            inputedValue = float(inputedValue)
            list_of_items_to_capture.append(inputedValue)
        except:
            print('bad data')
            #end of loop
#loop to find the max and min
max_variable = None
min_variable = None
for i in list_of_items_to_capture:
    #start with max
    if(max_variable is None or i > max_variable):
        max_variable = i
    if(min_variable is None or i < min_variable):
        min_variable = i
print("the maximum and minimum values are \n")
print(max_variable, min_variable)