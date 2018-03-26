# Classes & Objects

# self --------> this in java

# der __init__(self) -------> constructor in java

class Student :
	z=50 # class variable shared by all instances
	def __init__(self):
		self.x = 10
		self.y = 20
	def __init__(self, x, y):
		self.x = x # instance variable
		self.y = y
		
	def __display(self) :
		print (z)
		
		
# student = Student()
# print (student.x, student.y )

student = Student(56,89)

print (student.x, student.y )

#print ( student._Student__display(student))

print (getattr(student, 'x'))

print ("z variable:", Student.z)
print ("z variable:", student.z)


