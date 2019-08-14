#question:an employee gets 1.5 times the rate for hours worked above 40 hours



rate=0.0
hour=0.0
salary=0.0                     #initialize 
input_hours=input('enter hours:')
try:
    hours=float(input_hours)   #convert string to float
except value_error:
    print("please enter numeric input")
    quit()



input_rate=input('enter the rate:')
try:
    rate=float(input_rate)     #convert string to float
except value_error:
    print("please enter numeric input")
    quit()

if hours<40:#without overtime
    salary=hours*rate
if hours>=40:           #with overtime  
    additional=hours-40
    salary=(rate*40)+(1.5*rate*additional)
    
print("salary:",salary)





#enter hours:67

#enter the rate:2
#salary: 161.0