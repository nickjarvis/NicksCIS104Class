

def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

mylist = [1, 2, 3, 4]
mylist2 = [1, 2, 3, 4]

choplist = chop(mylist)
print(mylist)
print(choplist)

middlelist = middle(mylist2)
print(mylist2)
print(middlelist)
