f= open('BASICS PYTH/myfile.txt','r')  # Before performing any action we must open the file by using open() function 
# open("Path of the file to be opend","mode in which we want to open the file")
# here 'r' is the default mode in which we have opened the file. IT means we have opened the file the file in read mode. Since 'r' is the default mode its not necessary to write it in open() function, we can simply write f = open('path')

print(f) # f is not the contents of the file. It is a file object, which represents an open connection to the file.
# this will print the type of file, path of the file , mode in which the file is opend and text encoding used by python to read the file.

t= f.read() # reads the content in the file 
print(t)   # prints the content in the file 
f.close()  # closes the file

# we can aslo do this by a better apporach , which is by using "with" statement

#with creates a managed block where a resource is acquired at the beginning and automatically cleaned up at the end, even if an exception occurs.

with open('BASICS PYTH/myfile.txt','r') as f :
    print(f.read())
# here we dont need to close the file manually, with does that for us even when any error occurs.

''' Modes in file :
1. read(r) - opens file in read mode and gives error if file doesn exist.
2. write(w) - opens a file for writing only, creates a new file if the file doesn't exist. Using wirte mode overwrite the file's contents. 
3. append(a) - opens a file for appending only, creates a new file if the file doesn't exist. Unlike write it doesn't erease the content of the file, it simply add the new data at the end.
4. create(x) - creates a file and gives error if file already exist.
5. text(t) - we use this to specify how the file must be handeled. t mode is used to handel text file. There is no difference between 'r' and 'rt', 'w' and 'wt' since text mode is default.
6. binary(b) - used t open binary file. ex:- 'rb', 'wb' . '''
