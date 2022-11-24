import getpass
import random as ra
def printd(up,cp):
  print("||-------point---------||")
  print("||   user  |  computer ||")
  print("||    {}    |     {}     ||".format(up,cp))
  print("||-+-+-+-+-+-+-+-+-+-+-||")
def uw():
  print("^^^^^user is win^^^^^^")  
def cw():
  print("^^^^^computer is win^^^^^^")   
l=['Rock','Paper','Scissor']
p=[0,0]
print("Enter the numbers \n 1 :- Rock\n 2 :- Paper \n 3 :- Scissor\n")
u=int(input("select :- "))

if(u==1):
  u=l[0]
elif(u==2):
  u=l[1]
elif(u==3):
  u=l[2]  
else:
  print("invalide Choice ,please enter the number 1 to 3") 
c=ra.choice(l)
# ind=l.index(c)+1
print("user     :- {}\ncomputer :- {}".format(u,c))
if(u==c):
  print('Draw')
elif(u==l[0] and c==l[1] )  :
  p[1]=p[1]+1
  cw()
  printd(p[0],p[1])
elif(u==l[0] and c==l[2]) : 
  p[0]=p[0]+1
  uw()
  printd(p[0],p[1])
elif(u==l[1] and c==l[0]) : 
  p[0]=p[0]+1
  uw() 
  printd(p[0],p[1])
elif(u==l[1] and c==l[2]) : 
  p[1]=p[1]+1
  cw()
  printd(p[0],p[1])
elif(u==l[2] and c==l[1]) : 
  p[0]=p[0]+1
  uw() 
  printd(p[0],p[1])
elif(u==l[2] and c==l[0]) : 
  p[1]=p[1]+1
  cw() 
  printd(p[0],p[1])