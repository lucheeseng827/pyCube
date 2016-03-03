#!/usr/bin/python

#remove first line and making "cf:column" for every column in there


with open("file1.txt","r") as input:
    with open("file2.txt","wb+") as output: 
        for line in input:
			if  line=="1,23,3,5,5,87"+"\n":
				a = line
				b= a.split(',')
				c=[]
				for i in b:
					c.append("%s:%s"%(b[i],b[i]))				
				d=','.join(c)
				output.write(d)
			else:
				output.write(line)
				
				