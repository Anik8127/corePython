#Call by value
'''A call by value is a copy of the variable passed through the function.
Henceforth, changes inside the function doesn't change the variable itself.
used for immutable objects like integres, strings and tuples in python.'''

#Call by reference
''' A call by reference is actual memory of the variable or actual variable passed into the function.
And changes inside the function changes the original variables itself.
Used for mutable objects like lists, dictionaries & sets.'''

#Eg. Call by Value

def myfunc(x):
    x += 10 #Modifies the local copy of x
    print("Inside function:", x)

myfunc(5)
a = 5
myfunc(a)
print("Outside function:", a) #Original value of a remains unchanged

'''Hence in the above example, 5 is an integer which is immutable, when a function is defined using 
such variables, the same value doesn't changes outside the function.'''

#Eg. Call by Value
def myfunc(lst):
    lst.append(10)
    print("Inside function:", lst)

lst = [1, 2, 3]
myfunc(lst)
print("Outside function:", lst) #Original value of lst is changed

'''Hence in the above example, we can see that since, the list is crreated outside the function and the list 
is called inside the function, the changes made inside the function is reflected outside the function as well.
This is because, the list is mutable and the function is called by reference.'''





