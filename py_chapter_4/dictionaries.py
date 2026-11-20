#Dictionaries are used to store data values in key:value pairs.
#They are unordered, mutable and don't allow duplicate keys.

info = {
    "Name": "Shlok",
    "Age": "18",
    "Marks": "96.67",
    98: 67
}

print(info) #This will print info.
print(info["Name"]) #This will only print value assigned to the key "Name".
info["Age"] = 19 #This will update the value of the key "Age" to 19.
info["Surname"] = "Mandhane" #This will add a new key:value pair to the dictionary.
print(info) #This will print the updated dictionary.