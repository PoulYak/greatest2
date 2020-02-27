
from itertools import permutations
class Hero(object):
	def __init__(self, name, level, race):
		self.name = name
		self.level = level
		self.race=race		
		self.health=100
	def show_hero(self):
		self.you=True
		dicription=(' Your name :'+self.name+'\n You have level '+str(self.level)+'\n Your race is '+self.race+'\n health '+str(self.health))
		print(dicription)
	def level_up(self):
		self.level+=1
		print(self.level)
	def move(self):
		print('Hero '+self.name+' start moving...')


#jane = Hero('Jane', 3, 'Russian')
#jane.show_hero()
#jane.level_up()
#print(111111111111111111111111111111111111111111)
#tom=Hero('Tom',1,'Polak')
#tom.level_up()
#tom.move()


from math import hypot



def closest_pair(points):
    a={}
    for i in permutations(points, 2):
        a[hypot(i[0][0]-i[1][0], i[0][1]-i[1][1])]=i
        
    b=list(a.items())
    b.sort()
    return b[0][1]


import turtle
T=turtle.Turtle()
T.speed(100)
long=10
T.goto(-300,-300)
def six(w):
    for i in range(w):
        T.forward(long)
        T.left(90)
    


for i in range(300):
    six(4)
    long+=i/10
    


x=input()
