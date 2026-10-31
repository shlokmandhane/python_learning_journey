# A built-in data type that stores set of values.
# It can store elements of different types (integers, float, string, etc.)

marks = [85, 92, 78, 96, 88]
print(marks)
print(type(marks))
print(marks[3]) # Accessing the fourth element (index 3)
print(marks[0]) # Accessing the first element (index 0)

#Lists are mutable in python. Whereas, strings are immutable in python. This means that we can change the values of a list, but we cannot change the values of a string.
Student = ["Shlok", 95.5, 18, "Nashik"]
Student[0] = "Pari"
Student[3] = "Mumbai"
print(Student)