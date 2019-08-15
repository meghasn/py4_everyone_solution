#wap whch repeatedly reads number until programmer typres done
#once done is entered print total count and average of numbers
#if a user enters anything other than number detect error
def checkerror(input):
    try:
        val=float(input)
        return val
    except checkval:
        print("please enter a numeric value")
        quit()
        
if __name__=="__main__":
    count=0
    total=0.0
    av=0.0
    while True:
        num=input("enter the number:")#all inputs are initially taken as a string
        if num=="done":
            break
        else:
            number=checkerror(num)
            
            count=count+1
            total=total+number
            
    if count!=0:
        av=total/count
        
    print(total,count,av)
        



#enter the number:1

#enter the number:2

#enter the number:3

#enter the number:4

#enter the number:done
#10.0 4 2.5