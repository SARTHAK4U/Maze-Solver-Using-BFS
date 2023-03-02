import turtle
from collections import deque
from grid import grid
from setup import Main
from setup import Green
from setup import Yellow
from setup import Red
from setup import Pink
from setup import Blue

screen=turtle.Screen()
screen.bgcolor('grey')
screen.setup(1300,700)
screen.title('maze solver using BFS Algorithm')


def maze_form(grid):
    global s_x,s_y,e_x,e_y
    for y in range (len(grid)):
       for x in range(len(grid[y])):
         Char=grid[y][x]
         screen_x = -588+ (x * 24)     
         screen_y =  288-(y * 24) 

         if Char == '+':
           yellow.goto(screen_x,screen_y)
           yellow.stamp()
           walls.append((screen_x, screen_y))

         if Char == 'e':
           e_x=screen_x
           e_y=screen_y
           blue.goto(screen_x,screen_y)
           blue.stamp()

         if Char == 's':
           s_x=screen_x
           s_y=screen_y
           red.goto(screen_x,screen_y)
           red.stamp()
         if Char == " " or Char == "e":
                path.append((screen_x, screen_y))


def search(x,y):
  queue.append((x,y))
  soln[x,y] = x,y
  while len(queue)>0:
    x, y = queue.popleft() 
    if(x - 24, y) in path and (x - 24, y) not in visited:  
            soln[(x - 24, y)] = x, y   
            queue.append((x - 24, y))  
            visited.add((x-24, y))

    if (x, y - 24) in path and (x, y - 24) not in visited:  
            soln[(x, y - 24)] = x, y
            queue.append((x, y - 24))
            visited.add((x, y - 24))

    if(x + 24, y) in path and (x + 24, y) not in visited:  
            soln[(x + 24, y)] = x, y
            queue.append((x + 24, y))
            visited.add((x +24, y))

    if(x, y + 24) in path and (x, y + 24) not in visited: 
            soln[(x, y + 24)] = x, y
            queue.append((x, y + 24))
            visited.add((x, y + 24))
    pink.goto(x,y)
    pink.stamp()



def back_route(x,y):
  red.goto(x,y)
  red.stamp()
  while (x, y) != (s_x, s_y):
    x,y=soln[x,y]
    red.goto(x,y)
    red.stamp()



blue=Blue()
green=Green()
pink=Pink()
red=Red()
maze=Main()
yellow=Yellow()


queue = deque()
soln = {} 
walls = []
visited = set()
path = []


maze_form(grid)
search(s_x,s_y)
back_route(e_x, e_y)
blue.goto(s_x,s_y)
blue.stamp()
blue.goto(e_x,e_y)
blue.stamp()
turtle.exitonclick()






