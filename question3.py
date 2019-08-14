#wap to prompt for a score between 0.0 and 1.0
#if the score is out of range print an error message
#if the score is within range print the grade 

score=0.0 #initializing
grade=""

input_score=input("enter the score:")
try:
    score=float(input_score)
except value_error:
    print("bad score")
    quit()
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

print(grade)


#enter the score:.5
#f