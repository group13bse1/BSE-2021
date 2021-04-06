location = input("enter name of city \n")
payment = input("enter salary \n")

# prevent the program from exiting prematurely
try:
    # change the city name entered to small letters for easy comparison
    location = location.lower()
    payment = int(payment)
# constraints of the program
    if(location == "space"):
        choice = "Without a doubt, I’ll take it"
        # the variable choice will be used to output the results
    elif(location == "mbarara"):
        if(payment <= 4000000):
            choice = "No Thanks, I can find something better"
        else:
            choice = "Sure, I can work with this"
    elif(location == "kampala"):
        if(payment < 10000000):
            choice = "No way!"
        else:
            choice = "Sure, I can work with this"
    elif(payment >= 6000000):
        choice = "Sure, I can work with this"
    else:
        choice = "No Thanks, I can find something better"
#output the results
    print(choice)
except:
    #executes when there is an error.
    print("Error, failed to execute")