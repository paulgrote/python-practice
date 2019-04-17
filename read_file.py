#Reads file
filename = '2019.html'

with open(filename) as f_obj:
	contents = f_obj.read()
	
print(contents)
