#append() method
#Add single item at end of the list

newlist = [3, "Hey", 8, "My",8.6]
newlist.append("You")                       #It will add "You" item at end of the list
print(newlist)                                                                        


#insert() method
#It is used to add elements at the desired position, It requires two  arguments (position,value)

list = [1, ”You”,  8.9, ”Too”]
list.insert(3, 14)                          #Add new element 14 at position 3(index 3) in the list
print(list)


#extend() method
#You can add multiple elements at the same time at the end of the list with extend() method

list = [1, ”You”,  8.9, ”Too”]
list.extend(“Talat”, 1, 9.7)                 #Add multiple new elements like “Talat” , 1 , 9.7 at end of the list
print(list)


#count() method
#It returns the count of how many times a given object occurs in a List.

Num = [1, 4, 2, 9, 7, 8, 9, 3, 1]            #It will count how many times 9 occur in the list 
x = Num.count(9)
print(x)

#index() method
#it returns first occurrence in the list,it will return index of element    | SYNTAX  list.index(item)

list = [2, 5, 7.9, "You", "Home", 10]
p = list.index(5)                                 #it will show you index of '5' which is 1
print(p)

#sum method
#it calculate sum of all elements

list = [2, 5, 7, 9,10, 1, 20]
print(sum(list))                              #it will show you sum of all elements that is 54

 
