marks= [85, 92, 78, 96, 88]
print(marks[1:4]) #Ending index is not included.
print(marks[:4])  #it will automatically take the starting index as 0.
print(marks[0:])  #it will automatically take the ending index as the last.
#there are also negative indexes in list slicing.
print(marks[-4:-1]) #it will automatically take the starting index as -5 and ending index as -1.