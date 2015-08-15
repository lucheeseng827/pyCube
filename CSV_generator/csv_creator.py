import random
import sys
from random import randrange

var1= open("first.csv","wb")
for x in range(0,200):
    if x ==0:
	var1.write("field0"+","+"field1"+","+"field2"+","+"field3"+"\n")
    elif x!=0 and x!=200:
	var1.write(str(x)+","+str(random.random())+","+str(random.random())+","+str(random.random())+"\n")
    elif x==200:
	var1.close()
	break




	
	
	