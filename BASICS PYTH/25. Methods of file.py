with open('BASICS PYTH/myfile.txt','r') as f :
    while True :
        line = f.readline()    # readline() method read a single line from the file. If we want to read multiple line then we use a loop as we used here
        if not line :
            break 
        print(line)      # This prints everything in myfle.txt in string format .
# this program reads the file untill the line is present, as soon as line is not present it stops and prints a empty line in last.
# When you open a file, Python creates a file object (f). That file object maintains an internal file pointer (also called the cursor).
# Initially, the file pointer is at the beginning of the file.
# As we use readline () python reads and stores the value and then the pointer moves to the next line.

'''read() → everything → returns one string
readline() → one line → returns one string
readlines() → all lines → returns a list of strings'''

with open('myfile2.txt','w') as f2 :
    lines = ['line 1\n', 'line 2\n', 'line 3\n']
    f2.writelines(lines)    # The writelines method in python writes a swquence of strings to a file. The sequence can be of any iterable object, like list and tuple.
# Note that writelines doesn't add new lines on its own, we manually have to add \n for it.