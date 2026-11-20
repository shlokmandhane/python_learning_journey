#Nested dictionariess are sub-dictionaries that are stored as values in a dictionary. They allow you to create more complex data structures and organize information in a hierarchical manner.

Student = {
    "Name": "Shlok",
    "Age": 18,
    "Marks": {
        "Maths": 96.67,
        "Science": 98.5,
        "English": 95.0
    }
}

print(Student) #This will print the entire Student dictionary.
print(Student["Marks"]) #This will print the nested dictionary containing the marks.
print(Student["Marks"]["Maths"]) #This will print the value of the key "Maths" in the nested dictionary.