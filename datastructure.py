#List
#------------------------
# A list is an ordered collection of values

# list is mutable

b=[10,20]
nested = ["hello",2.0, 5, [10,20]]
print ( b[0])
print ( nested[3][1])


# possible operations
# concatenations
# memberships 
# for loop

print ( 3 in [1,2,3])
print ( ['hi'] * 4 ) # repeated in single list


# append, extend, pop , reverse, sort

c=[1,2]

print ( c)



# Tuple
#------------------------
# tuple is immutable


rec=("ruck",1235,10.5)

print ( rec)
print (type(rec))


# basic operations
# unpack
# swap
for x in (1,2,3):
	print ( (x))
# min, max

#Dictionary
#------------------------
# key value pair
# its mutable but keys immutable

dic = {'one': 'value','two':'value','three': None}

dic2 = {'four' : 'value'}

dic.update(dic2)

if dic['three'] == None : # not "None"
	print ("true its none ")
	
print (dic.keys())


print ( dic)



# SETS
#-------------------
# its a container to store unique elements

# for null or empty in other technologies but in python its none

basket=['apple', 'banana','apple']
fruit = set(basket)
print ( fruit)

# operations
# in, not in 



