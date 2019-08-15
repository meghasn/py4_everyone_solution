#wap that takes a list of number as the previous question and 
#print max and min out of it
def checkerror(input):
    try:
        val=float(input)
        return val
    except checkval:
        print("please enter a numeric value")
        quit()
number=input("enter a number")
if number=="done":
    quit()


num=checkerror(number)
smallest=num
largest=num
    
while True :
    number=input("enter a number")
    if number=="done":
        break
    else:
        
        num=checkerror(number)
        if num>largest:
            largest=num
        elif num<smallest:
            smallest=num


print(largest,smallest)



#enter a number2

#enter a number3

#enter a number1

#enter a numberdone
#3.0 1.0
    