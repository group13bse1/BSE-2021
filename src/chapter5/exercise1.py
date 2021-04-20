# strt with an empty list
list_of_items_to_capture = []
#create a loop for capturing values
random_number = 1
while random_number == 1:
    inputedValue = input('enter  values, else enter done\n')
    if len(value_to_be_checked) == 0:
        print('bad data')
    elif string.lower(value_to_be_checked) == "done":
        return 'end_program'
    else:
        try:
            value_to_be_checked = float(value_to_be_checked)
            return value_to_be_checked
        except:
            print('bad data')

