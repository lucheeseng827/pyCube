#!/usr/bin/python

#remove first line and making "cf:column" for every column in there


with open("file1.txt","r") as input:
    with open("file2.txt","wb") as output: 
        for line in input:
            if line!="line_string to be deleted"+"\n":
                output.write(line)