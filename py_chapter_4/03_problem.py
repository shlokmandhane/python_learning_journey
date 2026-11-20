#WAP to enter marks of three subjects from user and store them in a dictionary. Start an empty dictionary and add one by one. use subject name as key and marks as value.


marks = {}
maths = int(input("Enter maths marks:"))
marks.update({"maths": maths})

chem = int(input("Enter chem marks:"))
marks.update({"chem": chem})

phy = int(input("Enter phy marks:"))
marks.update({"phy": phy})

print(marks)
