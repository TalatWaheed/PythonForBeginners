#Python Tuple Methods
#Python has two built-in methods that you can use on tuple 
#1. count()
#2.  index()

#[1] Python Tuple count() Method
#It returns the count of how many times a given element occurs in a Tuple.
#Syntax        
Tuple.count(element)

#For Example

tuple = (1, 6,  8, 2, 10, 8, 1, 1)
t =tuple.count(8)
print(t)

#[2] Python Tuple index() Method
#It returns first occurrence of given element from the tuple
#Syntax
Tuple.index(element)

#For Example

tuple = (1, 6,  8, 2, 10, 8, 1, 1)
t =tuple.index(8)
print(t)

#It will print 2 because first occurrence of 8 element at “index 2”
