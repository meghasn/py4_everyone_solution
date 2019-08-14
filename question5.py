#rewrite your paycomputation with tym and a half for overtime
#and create a fn called compute pay which takes two parameters(hours and rate)

def compute_pay(hours,rate):
    if hours<=40:#without overtime
        return (hours*rate)
    else:         #with overtime  
        additional=hours-40
        return ((rate*40)+(1.5*rate*additional))
    
    
def check_float(input1):
     
    
    try:
        val=float(input1)   #convert string to float
        return val
    except value_error:
        print("please enter numeric input")
        quit()



salary=0.0                #initialize salary
input_hours=input('enter hours:')
input_rate=input('enter the rate:')
hours=check_float(input_hours)   #convert string to float
rate=check_float(input_rate)     #convert string to float    
salary=compute_pay(hours,rate)
print("salary:",salary)




#enter hours:45

#enter the rate:10
#salary: 475.0