str = "my name is Shlok."
print(str.endswith("lok."))              #str.endswith("") will return true if the string ends with substr.

print(str.capitalize())                  #str.capitalize() capitalizes the first character of the string.
#str = "my name is Shlok."
#str = str.capitalize()
#print(str)
#this commented method will help usto capitalize the first cahracter of the string as many times as we want.

print(str.replace("Shlok", "Ashish"))    #str.replace("old_substr", "new_substr") will replace the old substring with the new substring in the string.

print(str.find("o"))                     #str.find("") returns first index of first occurance of the substring in the string. If the substring is not found, it returns -1. We can also search for a word through this method.

print(str.count("s"))                    #str.count("") count the occurance of the substring in the string and returns the count.