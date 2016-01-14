import sys
import random
from random import randrange

pul = open("password.txt","ab") #wb typical new creation
passworda = []
alpha = ['a','b','c','d','e','f','g,','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numer = [1,2,3,4,5,6,7,8,9,0]
specialchar = ['!','@','#','$','%','^','&','*']

def state():
    for x in range(0,8):
        a =randrange(1,4)
        if a ==1:
            passworda.append(random.choice(alpha))
            b= randrange(0,1)
            if b ==0 :
                string = random.choice(alpha)
                passworda.append(str(string.upper()))
            else:
                passworda.append(random.choice(alpha))
        elif a ==2:
            passworda.append(random.choice(numer))
        elif a== 3:
            passworda.append(random.choice(specialchar))
            
            
def stringify():
    stringed = ''.join(str(passworda))
    new_stringed = stringed.replace("'","")
    new_stringed1 = new_stringed.replace(",","")
    new_stringed2 = new_stringed1.replace(" ","")
    pul.write(str(new_stringed2)+",")
    pul.write(str(passworda)+"\n")
    del passworda[:] 

    
    
        
def loop_state(n):
    for x in range(0,n):
        state()
        stringify()
        
        
        
        
loop_state(1000)
pul.close()
     

       
        


        
