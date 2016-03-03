#!/usr/bin/python
#this will put colon in between column family and column in the first line youwill to change both of the filename parameter

del_line = 1  #line to be deleted: 

with open("test1.txt","r") as textobj:
    lista = list(textobj)    #puts all lines in a list
b= lista[0].split(',')
print lista[0]
c=[]
#looping to make mutation cf:cf
for i in range(len(b)):
	c.append("%s:%s"%(b[i],b[i]))
	
#list comprehension
c = [g.replace('\n','') for g in c ]

		
c[-1]+'\n'
print c
d=','.join(c)#converting to long mutated string/line

	
del lista[del_line-1]    #delete regarding element
lista.insert(0, d) #inserting the new mutated line
				
 #rewrite the textfile from list contents/elements:
with open("test1.txt","w") as textobj:
    for n in lista:
		textobj.write(n)