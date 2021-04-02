location = input("enter name of city \n")
payment = input("enter salary \n")

try:
    location = location.lower()
    payment = int(payment)

    if(location == "space"):
        choice = "Without a doubt, I’ll take it"
    elif(location == "mbarara"):
        if(payment <= 4000000):
            choice = "No Thanks, I can find something better"
        else:
            choice = "Sure, I can work with this"
    elif(location == "kampala"):
        if(payment < 1000000):
            choice = "No way!"
        else:
            choice = "Sure, I can work with this"
    elif(payment >= 6000000):
        choice = "Sure, I can work with this"
    else:
        choice = "No Thanks, I can find something better"

    print(choice)
except:
    print("Error, failed to execute")