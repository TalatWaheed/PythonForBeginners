#Accessing  Tuple element
#[1]You can access them by referring index number
#Syntax
#tuple(index)

#For Example

tuple = (1, 6,  8, 2, 10)
print(tuple[1])

#[2]Access element with Negative indexing 
#It start from end of the list(right to left),Rightmost element has an index value of  -1
#For Example

tuple = (“Hey”,  3,  “I”,   7,  “Am”,   2)
#index    -6    -5   -4    -3    -2     -1  (Negative)   
print(tuple[-1])

#[3]Access element with Range of indexes
#It specifies where to start and where to end the range
#For Example

tuple = (“Hey”,  3,  “I”,  7,  “Am”,  2,  “Talat”)
#Index      0      1    2   3     4      5       6
print(tuple[2:5])


#If we leave the start value, then it will begin with the first item(index 1)
tuple = ("mango", "banana", "cherry", "orange", "kiwi", "apple")
print(tuple[:4])

#if we leave the end value, then it will go on to the end of the list
tuple = ("Black", "Blue", "White", "orange", "Green", "pink", "maroon")
print(tuple[5:])

#[4]Access element with Range of Negative indexes
#Specify negative indexes if you want to start the search from the end of the tuple
#For Example

tuple = ("apple", True, 9, "orange", 8.6, "melon", "mango")
print(tuple[-4:-1])

#Note - It returns the items from "orange" (-4) to, but NOT including "mango" (-1)


