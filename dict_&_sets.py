#Dictionaries

info = {"key": "values",
"name":"Aniket",
"age": "28",
"gender": "male",

}
print(info)


info = {"key": "values",
"name":("Aniket","Garima"),
"age": "28",
"gender": "male",

}
print(info)

#there is no order or index in dictonaries
#so we cannot use index to access the values in dictionary
#we can use keys to access the values in dictionary
#keys are unique in dictionary and not repeated

print(info["name"])

info = {"key": "values",
"name":("Aniket","Garima"),
"age": "28",
"gender": "male",

}

print(info["surname"]) #accessing the first element of the tuple in dictionary