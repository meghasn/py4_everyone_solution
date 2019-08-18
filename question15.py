"""
wap asking user for a list of numbers and print maximum and minimum at the end when the user enters done
"""
mylist=[]
while True:
    number=0.0
    in_number=input("enter the number:")
    if in_number=='done':
        break
    try:
        number=float(in_number)
    except valerror:
        print("invalid input")
        quit()
    mylist.append(number)
print("max:",max(mylist))
print("min:",min(mylist))



#enter the number:5

#enter the number:2

#enter the number:3

#enter the number:1

#enter the number:6

#enter the number:done
#max: 6.0
#min: 1.0