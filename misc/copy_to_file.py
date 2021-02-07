# Copy the contents of one .txt file and append to another .txt file.

# Specify the file names in the following variables.
filename1 = 'test1.txt'
filename2 = 'test2.txt'

# Opens and reads the first file and saves the contents to the lines variable.
with open(filename1) as f_obj:
	lines = f_obj.read()

#Opens the second file and appends the contents of the lines variable.	
with open(filename2, 'a') as f:
	f.write(lines)
