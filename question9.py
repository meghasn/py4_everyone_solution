#using a while loop read from last character of a string and print backwards

word=input("enter the string:")
index=len(word)-1
while index>=0:
    a=word[index]
    print(a)
    index=index-1
    
#enter the string:banana
#a
#n
#a
#n
#a
#b