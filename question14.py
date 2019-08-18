"""
write a fn that takes a list and modifies it
removing first and last element and return null
write a fn called middle that takes alist and returns a new list
that contains all but first and last element
"""

def chop (lst):
    del lst[0]
    del lst[-1]
def middle(lst):
    new=lst[1:]
    del new[-1]
    print(new)
    
lst=[1,2,3,4,5,6]
chop(lst)
middle(lst)


#[3, 4]