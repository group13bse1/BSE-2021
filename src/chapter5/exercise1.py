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
#create a loop that goes thru the list created above and creates total and count
total_variable = 0
counting_variable = 0
for iteration_variable in list_of_items_to_capture:
    total_variable = total_variable + iteration_variable
    counting_variable = counting_variable + 1
print("count, total, and average")
print(counting_variable, total_variable, total_variable/counting_variable)

