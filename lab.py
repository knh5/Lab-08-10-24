a = 11
b = 5
result = a < b
type_result = type(result)
print (f"result = {result} and its data type is {type_result}")

#this will print 14
x = 10
x = 14
print (x)

#this will print "please"
a = "Hello, I am here"
a = "please"
print(a)

#this will print 23
m = "this is a text"
m = 23
print(m)

#this variable holds my name and by specifing which position of the variable to 
#print starting at 0 i can print letters from my name or anything else held by the variable
unit_name = "Suhrab Shamshiri"
print("my name is ", unit_name)
print("It starts with ", unit_name[0])
print("It ends with ", unit_name[5])
print("My surname starts with ", unit_name[7])

greeting_string = "welcome to Programming unit! This is a level 4 unit :)"
print (greeting_string)
print (greeting_string[0])
print (greeting_string[4])
print(greeting_string[0:5])
print (greeting_string[-1])
print (greeting_string[-4:])
#greeting_string[0] = "x" strings are immutable

xx = "look! i will become the best python programmer"
yy = 10
zz = 5.5
#tasks 1-4
type_resultt = type(xx)
type_resulttt = type(yy)
type_resultttt = type(zz)
resultt = yy+zz
type_resulttttt = type(resultt)
print (type_resultt)
print (type_resulttt)
print (type_resultttt)
print (f"result = {resultt} and its type is {type_resulttttt}")
#task 5
resulttt = yy+int(zz)
type_resultttttt = type(resulttt)
print (f"result = {resulttt} and its type is {type_resultttttt}")
#task 6
resulty = zz + float(yy)
type_resulty = type(resulty)
print (f"result = {resulty} and its type is {type_resulty}")
#task 7
bb = str(zz)
type_result_1 = type(bb)
print (type_result_1)
#task 8
cc = xx + str(yy) + str(zz)
type_result_2 = type(cc)
print (f"result = {cc} and its type is {type_result_2}")
#task 9
dd = xx + yy
print (dd)