#You can remove elements in list with help of list methods #remove(), #pop() , #clear()

#remove() method
#It removes  element with specified value, Note-It removes only first occurrence element of the list

list = [1, ”You”,  8.9, ”Too”]
list.remove(“You”)                                 #Remove “You” element from the list
print(list)


#pop() method
#Remove element at specified position, By default it removes only the last element of the list

list = [1, ”You”,  8.9, ”Too”]
list.pop(1)                                         #Remove “You”element at index of 1 in the list
print(list)


#clear() method
#It removes all elements from the list

list = [1, ”You”,  8.9, ”Too”]
list.clear()                                        #Removes all elements of the list
print(list)
