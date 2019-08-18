count=0
total=0
fname=input("enter the name of file:")
try:
    fhand=open(fname)
except errorfilenotfound:
    print("file not found")
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        colpos=line.find(':')
        number=line[colpos+1:].strip()
        SPAM_C=float(number)
        total=total+SPAM_C
average=total/count
print(average)


#0.8475