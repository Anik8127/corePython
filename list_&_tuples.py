marks = [94.4,95,92.8,96.66]
print(marks[0])
#Note strings are immutable, so we cannot change the string in the list
str = 'hello'
str[0] = 'H' # This will give an error
#Furthermore, we can mutate the list
student = ['Arjun',97.7,17,'New Delhi']
student[0] = 'Karan' # This will work
print(student)

#Slicing & indexing
marks = [94,93,91,96,89,95]
print(marks[ :5]) # is same as marks[0:5]
marks = [94,93,91,96,89,95]
print(marks[1:4]) # is same as marks[1:4]
marks = [94,93,91,96,89,95]
print(marks[ : ]) # is same as marks[0:6]
marks = [94,93,91,96,89,95]
print(marks[ : :2]) # is same as marks[0:6:2]
marks = [94,93,91,96,89,95]
print(marks[2: ]) #is same as marks[2:len(marks)]
#Indexes with step
marks = [94,93,91,96,89,95]
print(marks[ 0:4:1]) #is same as marks[0:4]

#Negative indexes
marks = [94,93,91,96,89,95]
print(marks[-1]) # is same as marks[len(marks)-1]
marks = [94,93,91,96,89,95]
print(marks[-4:-1]) 
#Negative indexes with step
marks = [94,93,91,96,89,95]
print(marks[-1:-4:-1]) # is same as marks[len(marks)-1:len(marks)-4:-1] or printing in reverse order
marks = [94,93,91,96,89,95]
print(marks[-1:-6:-2]) # is same as marks[len(marks)-1:len(marks)-6:-1]

marks = [94,93,91,96,89,95]
print(marks[-6]) # is same as marks[0]