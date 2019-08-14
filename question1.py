#question:an employee gets 1.5 times the rate for hours worked above 40 hours

salary=0.0                     #initialize salary
input_hours=input('enter hours:')
input_rate=input('enter the rate:')
hours=float(input_hours)   #convert string to float
rate=float(input_rate)     #convert string to float

if hours<40:#without overtime
    salary=hours*rate
if hours>=40:           #with overtime  
    additional=hours-40
    salary=(rate*40)+(1.5*rate*additional)
    
print("salary:",salary)





#enter hours:67

#enter the rate:2
#salary: 161.0