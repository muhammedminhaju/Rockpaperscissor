import random as ra
def decision(c,u,p):
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
def final(up,cp):
  print("||---------------------||")
  print("||        Exit         ||")
  print("||---------------------||") 
  printd(up,cp)
  if(up>cp):
   print("\n||=====================||")
   print("||     Final Winer     ||")
   print("||---------------------||") 
   print("||   ***** USER *****  ||")
   print("||=====================||") 
  elif(cp>up) :
   print("\n||=====================||")
   print("||     Final Winer     ||")
   print("||---------------------||") 
   print("||  *** COMPUTER ***   ||")
   print("||=====================||") 
  else:
   print("\n||=====================||")
   print("||     Final Winer     ||")
   print("||---------------------||") 
   print("||  ***** Draw *****   ||")
   print("||=====================||") 
def ins1():
  print("\n||---------------------||")
  print("||  Enter the numbers  ||")
  print("||---------------------||") 
  print("||       1 :- Rock     ||")  
  print("||       2 :- Paper    ||") 
  print("||       3 :- Scissor  ||") 
  print("||       4 :- Exit     ||")
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
def checkingandchanging(c,u,p):
 if(u==1):
  u=l[0]
  return u
 elif(u==2):
  u=l[1]
  return u
 elif(u==3):
  u=l[2]
  return u  
 else:
  print("invalide Choice ,please enter the number 1 to 3 if you want to play countinous ")
def ins11():
 c=ra.choice(l)
 ins1()  
 u=int(input("||    user select :-   ||=>"))
 return c,u
l=['Rock','Paper','Scissor']
p=[0,0]
c,u=ins11()
while(True):
 if(u==4):
   final(p[0],p[1])
   break
 u=checkingandchanging(c,u,p) 
 ins2(c,u) 
 decision(c,u,p)
 c,u=ins11()
