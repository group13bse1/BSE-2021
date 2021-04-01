age = input("enter your age \n")
try:
    age = int(age)
    if (age >= 18):
        print("you can vote")
    elif(age > 0 and age <= 17):
        print("too you to vote")
    else:
        print("you are a time traveller")

except:
    print("Error, enter numeric value")