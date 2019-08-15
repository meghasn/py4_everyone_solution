#encapsulate the code in a fn named count and generalize it so that it accepts the string and letter as arg

def count(string,letter):
    counter=0
    for i in string:
        if(i==letter):
            counter=counter+1
    print(counter)





string=input("enter the string")
letter=input("enter the letter")
count(string,letter)


#enter the stringbanana

#enter the lettera
#3