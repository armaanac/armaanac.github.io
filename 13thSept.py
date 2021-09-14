'''
print('hello world')
print ('goodbye world')

var1 = 'hello'
var2 = 'world'
var3 = var1 + '' + var2
print(var3)

# comment is anything that begins with a hashtag, comments are codes that doesn't get executed
'''

#anything between triple quotes also comment
'''
#INT
x= 1
y = 5
z = 5*(x+y)
print (z)

# 5** is 5 raised to the power
# for integers, python is always going to give you exact results, there are no size limits
#non-integer numbers; (fractions, irrational numbers) are approximations

#FLOAT
x = 0.1
y = 0.1
z = 0.1
q = x+y+z
print (q)

#variable value is changed, coz x was earlier = 1, now x = 0.1

#Type of a number with a period is called a float, type of number with no period is called an Int 
#the last type is the str ='string', for strings

#STR
x = 'this is a string'
print (x)

#python is an 'untyped language' because we can change the type
'''

#pseudocode for the quadratic formula
# a(**2 +- sqrt (b-4ac))/ 2a

#import is a keyword; math is library/package we are importing 
import math
'''
a = 5
b = 100
c = 2
quadratic1 = (a**2 + math.sqrt(b- 4 * a * c))/(2 * a)
quadratic2 = (a**2 - math.sqrt(b- 4 * a * c))/(2 * a)
print (quadratic1)
print (quadratic2)

a = 3 
#to update a = 3 we need to paste the quadratic formulas down as well
quadratic1 = (a**2 + math.sqrt(b- 4 * a * c))/(2 * a)
quadratic2 = (a**2 - math.sqrt(b- 4 * a * c))/(2 * a)
print (quadratic1)
print (quadratic2)
'''
#functions + variables are the key difference between Python and HTML/CSS
#def means function
'''
def quadratic (a, b, c) #a,b,c are parameters
    result = (a**2 - math.sqrt(b - 4 * a * c))/ (2 * a)
    return result
    # if you print (result), doesnt let you use the value; DONT DO THIS - dont use print

print (quadratic (5, 100, 2))
print (quadratic (3, 100, 2))

'''
#False and True are boolean values
'''
x = 5
y = 7
print (x < y)

#To check if 2 things are equal to each other, do x == y - see boolean logic Python cheatsheet

'''

x = 5
y = 26
print (y//x) #to get an integer and NOT decimal value after divison
print (y%x ) #modulus operation to get remainder

'''
quadratic_formula #this is called snake case -- use this
quadraticFormula #this is called camel case


