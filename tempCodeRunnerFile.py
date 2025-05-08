#Eg. Call by Value
def myfunc(lst):
    lst.append(10)
    print("Inside function:", lst)

lst = [1, 2, 3]
myfunc(lst)
print("Outside function:", lst) #Original value of lst is changed