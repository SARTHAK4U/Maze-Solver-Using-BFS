import turtle
board=turtle.Turtle


class Main(board):
     def __init__(self):
       board.__init__(self)
       self.shape('square')
       self.color('white')
       self.penup()
       self.speed(0)


class Green(board):
     def __init__(self):
       board.__init__(self)
       self.color('green')
       self.shape('circle')
       self.penup()
       self.speed(0)

class Yellow(board):
     def __init__(self):
       board.__init__(self)
       self.color('yellow')
       self.shape('circle')
       self.penup()
       self.speed(0)
 
class Red(board):
     def __init__(self):
       board.__init__(self)
       self.color('red')
       self.shape('square')
       self.penup()
       self.speed(0)

class Pink(board):
     def __init__(self):
       board.__init__(self)
       self.color('pink')
       self.shape('circle')
       self.penup()
       self.speed(0)
class Blue(board):
     def __init__(self):
       board.__init__(self)
       self.color('blue')
       self.shape('circle')
       self.penup()
       self.speed(0)
