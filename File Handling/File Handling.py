# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+: To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.


# Writing Mode
file = open('Dharni.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# Reading Mode
file =open("Dharni.txt","r")
for each in file:
    print(each)


# Append Mode
file =open("Demo.txt","a")
file.write("Hello World!!")


# r+
file =open("Demo.txt","r+")
file.write("Hi ")


# w+
file =open("Demo.txt","w+")
file.write("Hi ")



# a+
file =open("Dharni.txt","a+")
file.write(" Hi ")



import os
def create_file(filename):
    try:
        with open(filename,"w") as f:
            f.write("Hello World")
        print("File" +" " + filename + " " + "created successfully")
    except IOError:
        print("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename,"r") as f:
           contents=  f.read()
        print(contents)

    except IOError:
        print("Error: could not read file " + filename)


def append_file(filename,text):
    try:
        with open(filename,"a") as f:
            f.write(text)
        print("Text appended to the file" + " " + filename + " " + "text added successfully ")

    except IOError:
        print("Error: could not append file " + filename)


def rename_file(filename,new_filename):
    try:
       os.rename(filename,new_filename)
       print(filename + " " + "renamed to" + " " + new_filename + " " + "successfully")
    except IOError:
        print("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        print(filename + " " + "removed" + " " +  "successfully")
    except IOError:
        print("Error: could not delete file " + filename)



create_file(filename="Demo.txt")
read_file(filename="Demo.txt")
append_file(filename="Dharni.txt",text="This is some additional information")
rename_file(filename="Demo2.txt",new_filename="Demo1.txt")
delete_file(filename="Demo.txt")