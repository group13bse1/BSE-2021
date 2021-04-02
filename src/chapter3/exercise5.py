people = input("enter number of guests \n")
try:
    people = int(people)
    if(people > 0 and people <= 50):
        price = 4000
    elif(people >50 and people <= 100):
        price = 10000
    elif(people > 100 and people <= 200):
        price = 15000
    elif(people > 200):
        price = 20000
    print(price)
except:
    print("Error, not valid")