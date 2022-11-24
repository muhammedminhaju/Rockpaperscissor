import random as ra
def final(p):
  print("exit")
def ins1():
  print("\n||---------------------||")
  print("||  Enter the numbers  ||")
  print("||---------------------||") 
  print("||       1 :- Rock     ||")  
  print("||       2 :- Paper    ||") 
  print("||       3 :- Scissor  ||") 
  print("||---------------------||") 
def ins2(c,u):  
  print("||---------------------||") 
  ul=len(u)
  cl=len(c)
  if(ul==7):
    usl=" "
  elif(ul==4):
    usl='    ' 
  else:
    usl="   " 
  if(cl==7):
    csl=" "
  elif(cl==4):
    csl='    ' 
  else:
    csl="   "   
  print("||   user   :- {}{}||".format(u,usl))
  print("|| computer :- {}{}||".format(c,csl))
  print("||---------------------||")
def printd(up,cp):
  print("||---------------------||")
  print("||       point         ||")
  print("||---------------------||")
  print("||   user  |  computer ||")
  print("||---------------------||")
  print("||         |           ||")
  print("||    {}    |      {}    ||".format(up,cp))
  print("||         |           ||")
  print("||-+-+-+-+-+-+-+-+-+-+-||\n")
def uw():
  print("||---------------------||") 
  print("||     user is win     ||") 
  print("||---------------------||") 
def cw():
  print("||---------------------||") 
  print("||   computer is win   ||") 
  print("||---------------------||")  
def draw():
  print("||---------------------||") 
  print('||         Draw        ||')
  print("||---------------------||") 
l=['Rock','Paper','Scissor']
p=[0,0]
c=ra.choice(l)
ins1()  
u=int(input("||       select :-     ||=>"))
while(True):
 if(u==4):
   final(p)
   break
 if(u==1):
  u=l[0]
 elif(u==2):
  u=l[1]
 elif(u==3):
  u=l[2]  
 else:
  print("invalide Choice ,please enter the number 1 to 3 if you want to play countinous ") 
 ins2(c,u) 
 if(u==c):
   draw()
   printd(p[0],p[1])
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
 c=ra.choice(l)
 ins1()  
 u=int(input("||       select :-     ||=>"))  