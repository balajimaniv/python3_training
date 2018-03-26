# Functions: parameter passing


def hello(greeting='Hello', name='world') :
	print('%s, %s!' %(greeting, name))

#call function
hello('Greetings')

hello('one', 'two')

# keyword argument
hello(name='balaji', greeting='hello greeting')

# thrwo error TypeError: hello() got multiple values for argument 'greeting'
# hello('greetings !!!',greeting='greet')
def print_params(x,y,z,*pospar, **keypair):
	print (x,y,z)
	print (pospar)
	print (keypair)
print_params(1,2,3,4,5,6,foo=1,bar=2)

print_params(z=4,y=6,x=4)

# print_params() thrwo error



# pass by reference
def display(mylist) :
		mylist.append([1,2]);
		print (mylist)
		return

mylist = [10,20]		
		
display(mylist)



# pass by values

mylist = [10,20]	
def display(mylist) :
		# mylist.append([1,2]);
		print (mylist)
		return
			
display([5,5])
print (mylist)


# Lamda functions
# ------------------
# unnamed functions


sum_1 = lambda x,y : x+y
print (sum_1(10,20))









