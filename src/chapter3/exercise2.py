hours = input('Enter Hours \n')
rate = input('Enter Rate\n')
try:
    hours = int(hours)
    rate = float(rate)
    if (hours <= 40):
        pay = rate*hours
    else:
        extra_time = hours - 40
        pay = (rate*hours) + ((rate*extra_time)/2)
    print('Pay: ', pay)
except:
    print("error, please enter a numeric input")