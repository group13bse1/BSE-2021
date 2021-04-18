#we will re-write the grade program using a function
#we start with function
def computegrade(score):
    if (score >= 0.9):
        grade = "A"
    elif (score >= 0.8):
        grade = "B"
    elif (score >= 0.7):
        grade = "C"
    elif (score >= 0.6):
        grade = "D"
    else:
        grade = "F"
    return(grade)

#get the input
scores = input("Enter score between 0.0 and 1.0 \n:\t")
#check that there is some input.
if len(scores) > 0:
    try:#convert string input to float
        float_score = float(scores)
        if(float_score < 1.0 and float_score >0.0):
            #call the function that was created
            computed_grade = computegrade(float_score)
            print(computed_grade)
        else:
         print("Error, value entered is not in range.")
    except:
        print("Error, please enter numeric value")
else:
    print("please enter a value")