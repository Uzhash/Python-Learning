# a="1"
# # a=2
# b="1"
# # b=2
# print(int(a)+int(b))

string="15"
number=7
string_number=int(string)
sum=number+string_number
print("the sum of both numbers is: ",sum) #this is explicit type conversion where we are converting string to integer before performing addition.

a=7
print(type(a))
b=3.0
print(type(b))
c=a+b
print(c)
print(type(c)) #this is implicit type conversion where we are adding an integer and a float, and the result is automatically converted to a float.