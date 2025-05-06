# marks = [94.4,95,92.8,96.66]
# print(marks[0])
# #Note strings are immutable, so we cannot change the string in the list
# str = 'hello'
# str[0] = 'H' # This will give an error
# #Furthermore, we can mutate the list
# student = ['Arjun',97.7,17,'New Delhi']
# student[0] = 'Karan' # This will work
# print(student)

# #Slicing & indexing
# marks = [94,93,91,96,89,95]
# print(marks[ :5]) # is same as marks[0:5]
# marks = [94,93,91,96,89,95]
# print(marks[1:4]) # is same as marks[1:4]
# marks = [94,93,91,96,89,95]
# print(marks[ : ]) # is same as marks[0:6]
# marks = [94,93,91,96,89,95]
# print(marks[ : :2]) # is same as marks[0:6:2]
# marks = [94,93,91,96,89,95]
# print(marks[2: ]) #is same as marks[2:len(marks)]
# #Indexes with step
# marks = [94,93,91,96,89,95]
# print(marks[ 0:4:1]) #is same as marks[0:4]

# #Negative indexes
# marks = [94,93,91,96,89,95]
# print(marks[-1]) # is same as marks[len(marks)-1]
# marks = [94,93,91,96,89,95]
# print(marks[-4:-1]) 
# #Negative indexes with step
# marks = [94,93,91,96,89,95]
# print(marks[-1:-4:-1]) # is same as marks[len(marks)-1:len(marks)-4:-1] or printing in reverse order
# marks = [94,93,91,96,89,95]
# print(marks[-1:-6:-2]) # is same as marks[len(marks)-1:len(marks)-6:-1]

# marks = [94,93,91,96,89,95]
# print(marks[-6]) # is same as marks[0]

# #Methods in python
# ###append() method
# # append() method is used to add an element at the end of the list
# mylst = [1,2,3,4,5]
# mylst.append(6)
# print(mylst) # [1,2,3,4,5,6]

# #sorting or list.sort() method, sorting means ascensing or desecending order
# mylst = [3,1,5,2,4]
# mylst.sort() # sort the list in ascending order
# print(mylst.sort()) # returns None
# print(mylst)

#  #Methods in python
# mylst = [3,1,5,2,4]
# mylst.append(6)
# print(mylst) # [1,2,3,4,5,6]

# mylst = [3,1,5,2,4]
# mylst.sort()
# print(mylst) # [1,2,3,4,5,6]

# mylst = [3,1,5,2,4]
# mylst.sort(reverse=True) # sort the list in descending order
# print(mylst) # [6,5,4,3,2,1]

# mylst = ["a","b","c","d","e"]
# mylst.reverse()
# print(mylst)

# mylst = [3,1,5,2,4]
# mylst.reverse()
# print(mylst)

# mylst = [3,1,4,8,9,2,5,7,6]
# mylst.insert(3,11) # insert 11 at index 3
# print(mylst)

# mylst = [3,1,4,8,9,2,5,7,6]
# mylst.remove(4) # remove 4 from the list
# print(mylst) # [3,1,8,9,2,5,7,6]

# mylst = [3,1,4,8,9,2,5,7,6]
# mylst.pop(2) #index pe jaake remove krna
# print(mylst)



# ########...............TUPLES.................##########


# mytup = (36,77,89,56,44,27)
# print(type(mytup)) # <class 'tuple'>
# mytup[0] = 100 # This will give an error
# #assignment in tuple is not allowed

# mytup = (1+2) #empty tuple
# print(type(mytup))

# #slicing in tuple

# mytup = (1,2,3,4,5,6,7,8,9)
# print(mytup[1:3]) # (2,3)

# # Slicing in tuples works same as the list

# ####Methods in Tuples####

# tup = (2,1,3,4,5,6,3,8,9)
# print(tup.index(3))


# tup = (2,1,3,4,5,6,3,8,9)
# print(tup.count(3)) # count the number of times 3 appears in the tuple


# ######Practise#########

# #1. WAP to ask the user to enter 3 movies and store them in a list

# movies = []

# mov1 = input("Enter movie name")
# mov2 = input("Enter movie name")
# mov3 = input("Enter movie name")        

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# #OR

# movies = []

# mov1 = movies.append(input("Enter movie name:"))
# mov2 = movies.append(input("Enter movie name:"))
# mov3 = movies.append(input("Enter movie name:"))

# print(movies)


#WAP to check if a list contains a palindrome of elements. (Hint: use copy() method())

mylst1 = [1,2,1]

mylst2 = mylst1[::-1]
print(mylst2)

if mylst1 == mylst2:
    print("List is palindrome")
else:   
    print("List is not palindrome") 