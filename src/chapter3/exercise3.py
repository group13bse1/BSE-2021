score = input("enter score between 0.0 and 1.0 \n")
try:
    score = float(score)
    if(score < 1.0 and score >0.0):
        if (score >= 0.9):
            grade = "A"
        elif(score >= 0.8):
            grade = "B"
        elif(score >= 0.7):
            grade = "C"
        elif(score >= 0.6):
            grade = "D"
        else:
            grade = "F"
        print(grade)
    else:
        print("error, value entered is not in range.")

except:
    print("enter numeric value")