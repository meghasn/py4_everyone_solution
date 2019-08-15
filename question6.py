#use fn computegrade that takes a score as parameter and return grade
def computegrade(score):
    grade=0.0
    if 0.0<=score<=1.0: #condition as per the question
        if score>=.9:
            grade="a"
        elif score>=.8:
            grade="b"
        elif score>=.7:
            grade="c"
        elif score>=.6:
            grade="d"
        else:
            grade="f"
    else:
        grade="bad score"
    return grade
        
input_score=input("enter the score:")

try:
    score=float(input_score)
except value_error:
    print("bad score")
    quit()
    
gr=computegrade(score)
print("grade",gr)



#enter the score:.78
#grade c