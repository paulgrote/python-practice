#Reads file
filename = 'test1.txt'

with open(filename) as f_obj:
	contents = f_obj.read()
	
print(contents)
