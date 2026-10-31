#slicing is used for accessing the parts of index.
#[starting_index : ending_index] 
#ening index isnt included in the output.

str = "shlok"
print(str[1:4])
#whenever, we have to include last index, we can simply type len(str).
#also, if we miss the starting index, then it will start from index 0.
#and if we miss the last index, then it will go till the end of the string.


#negative index:
str = "ashish"
print(str[-3:-1])  #it will start from the end of the string and go backwards.