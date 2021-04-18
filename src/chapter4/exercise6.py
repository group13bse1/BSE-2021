#we will re-write the pay program using a function

#we will start with computepay function
def computepay(hours, rate):
    # when the hours are less than 40, the pay is calculated normally
    if (hours <= 40):
        pay = rate*hours
    else:
    # other wise the pay is the sum of the Full pay
    # and the half computational pay for the overtime
        extra_time = hours - 40
        pay = (rate*hours) + ((rate*extra_time)/2)
    return pay

#the inputs are still the same.
#note. to avoid confusion, we will use hrs and rt for hours and rate outside our function
hrs = input('Enter Hours \n:')
rt = input('Enter Rate\n:')
# print(computepay(hrs, rt))
if len(hrs) > 0 and len(rt) > 0:
    try:
        hrs_ver = float(hrs)
        rt_ver = float(rt)
        return_value = computepay(hrs_ver, rt_ver)
        print(return_value)
    except:
        print("error, please enter a numeric input")
else:
    print("Enter something and try again!")

