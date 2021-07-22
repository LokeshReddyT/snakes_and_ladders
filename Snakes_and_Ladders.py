import random
import time
snakeladders={}
for i in range(5):
  p=random.randrange(0,60)
  q=random.randrange(p+10,99)
  r=random.randrange(21,99)
  s=random.randrange(1,r-10)
  snakeladders[p]=q
  snakeladders[r]=s
opt1={}
def opt():
  adv=[91,90,71,70,51,50,31,30,11,10]
  b=[]
  a=100
  for i in range(10):
    for j in range(10):
      b.append(a)
      a=a-1
    for k in range(10):
      if i%2==0:
        if b[k] in adv:
          if b[k] in opt1:
            b[k]=opt1[b[k]]
            print("|   ",b[k],"   |",end="  ")
          else:
            print("|   ",b[k],"   |",end="  ")
        else:
          if b[k] in opt1:
            b[k]=opt1[b[k]]
            print("|   ",b[k],"   ",end="  ")
          else:
            print("|   ",b[k],"   ",end="  ")
      else:
        c=b[::-1]
        if i==9:
          if c[k] in adv:
            if c[k] in opt1:
              c[k]=opt1[c[k]]
              print("|    ",c[k],"   |",end="  ")
            else:
              print("|    ",c[k],"   |",end="  ")
          else:
            if c[k] in opt1:
              c[k]=opt1[c[k]]
              print("|    ",c[k],"   ",end="  ")
            else:
              print("|    ",c[k],"   ",end="  ")
        else:
          if c[k] in adv:
            if c[k] in opt1:
              c[k]=opt1[c[k]]
              print("|   ",c[k],"   |",end="  ")
            else:
              print("|   ",c[k],"   |",end="  ")
          else:
            if c[k] in opt1:
              c[k]=opt1[c[k]]
              print("|   ",c[k],"   ",end="  ")
            else:
              print("|   ",c[k],"   ",end="  ")
    print (" ")
    for l in range(19):
      print("-------",end="")
    print(" ")
    b=[]

def sladder(a):
  if a in snakeladders:
    if a>snakeladders[a]:
      print("snake bite you😭😭😭")
    else:
      print("you hit ladder🎉🎉🎉")
    return snakeladders[a]
  else:
    return a
def counts():
  a=0
  for i in range(len(players_name)):
    if players_list[players_name[i]]==100:
      a=a+1
  return a
players_list={}
players_name=[]
opt3=[]
k=0
print('''Welcome to snakes and ladders game. In this game 
you can play as many as people you can. player who scored
 100 will win the game''')
print('''🚫🚫🚫NOTE:-Each time the positions of snakes and
 ladders will change''')
print("enter no of players")
no_of_players=int(input())
for i in range(no_of_players):
  print("enter player",i+1,"name")
  player_name=input()
  print(player_name,"enter your character to represent it in the game board")
  opt4=input()
  opt3.append(opt4)
  players_name.append(player_name)
  players_list[player_name]=0
print("snakes and ladders for this game are",snakeladders)
while True:
  if players_list[players_name[i]]==0:
    opt()
  if players_list[players_name[k]]<100:
    print("press any key to roll the die",players_name[k])
    useless=input()
    die=random.randrange(1,7)
    print("you got",die)
    players_list[players_name[k]]=players_list[players_name[k]]+die
    players_list[players_name[k]]=int(sladder(players_list[players_name[k]]))
  if players_list[players_name[k]]>100:
    players_list[players_name[k]]=players_list[players_name[k]]-die
    print("unable to move forward, your points are",players_list[players_name[k]])
  else:
    print("your total points are",players_list[players_name[k]])
  
  for i in range(len(players_name)):
    if players_list[players_name[i]] not in opt1:
      opt1[players_list[players_name[i]]]=opt3[i]
    else:
      uuu=str(opt1[players_list[players_name[i]]]+opt3[i])
      opt1[players_list[players_name[i]]]=uuu
  opt()
  opt1={}
  
  count=int(counts())
  if count+1==no_of_players:
    break
  k=k+1
  if k==no_of_players:
    k=0
for i in range(no_of_players):
  if players_list[players_name[i]]!=100:
    print(players_name[i],"loose the game")

