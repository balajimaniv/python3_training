#if
---------------------------

var1 = 100

if var1:
	print ("got it, as non zero")
	print (var1)
print ('outside if')


# if .. else
---------------------------
var1=0

if var1:
	print ("got it, as non zero")
	print (var1)

else :
	print ("got it, its zero")


# if .. elif..else
---------------------------
var1=100
if var1 ==200 :
	print ("exact 200")
	print (var1)

elif var1 == 100 :
	print("exact 100")

else :
	print ("got it, its zero")




# loops
---------------------------
# for loop --- finite number known
---------------------------



# while loop ---- 
---------------------------
count=0
while(count < 9) :
	print ("count",count)
	count+=1 # count=count+1



# while with else
---------------------------
#while expression:
#	statement(s)
#else :
#	statements

count=5
while(count < 5) :
	print ("count",count)
	count+=1 # count=count+1
else :
	print ("out of loop")





# simple for loop
---------------------------

# applicable for list, tuple

print("list of fruits")
fruits = ['mango','apple', 'orange']
for fruit in fruits :
	print (fruit)


# for with else
---------------------------


# break, continue, pass

# pass
# inorder to show sytactactically some some statements there for that we have to use pass
