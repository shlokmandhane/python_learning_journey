Student = {
    "Name": "Shlok",
    "Age": 18,
    "Marks": {
        "Maths": 96.67,
        "Science": 98.5,
        "English": 95.0
    }
}

#myDict.keys(). this returns all keys.
print(list(Student.keys()))#This will print all the keys in the Student dictionary.
print(len(Student))

#myDict.values(). this returns all values.
print(Student.values()) #This will print all the values in the Student dictionary.

#myDict.items(). this returns all items in the dictionary as a list of tuples.
print(Student.items())
pairs = list(Student.items())
print(pairs[0]) #This will print the first item in the list of tuples.

#myDict.get("key"). Returns the key according to the value.
print(Student.get("Name"))
print(Student.get("Name2")) #This will return None as the key "Name2" does not exist in the dictionary.

#myDict.update(new dict). This method updates the dictionary with the key-value pairs from new_dict.
Student.update({"City": " Mumbai"})
new_dict = {"Class": "A"}
Student.update(new_dict)
print(Student)