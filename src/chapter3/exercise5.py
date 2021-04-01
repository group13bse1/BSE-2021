people = input("enter number of guests \n")
try:
    people = int(people)
    if(people > 0 and people <= 50):
        price = 4000
    elif(people >50 and people <= 100):
        price = 10000
    elif(people > 100 and people <= 200):
        price = 15000
    elif(people > 200 and people > 200): #i added an extra elif. to check negative. but when we put a negative while testing it executes both line 13 and 16.
        price = 20000
    else:
        print("Error, people cannot be negative ")
    print(price)
except:
    print("Error, not an integer")