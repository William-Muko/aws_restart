#string data type
myString="This is a String."
print(myString) 
print(type(myString)) 
print(myString + " is of data type " + str(type(myString))) 



#String Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString) 



#Input String
name = input("What is your name?") 
print(name) 



#Format Output
color = input("What is your favorite color?")  
animal =input("What is your favorite animal?") 
print("{}, you like a {} {}!".format(name,color,animal))