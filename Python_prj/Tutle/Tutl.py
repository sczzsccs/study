{# from turtle import *

# shape()

# color("black", "red")
# pencolor("Green")
# begin_fill()
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)
# left(120)
# end_fill()
# goto(-100, 0)
}

import turtle

class My_Turtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.pensize(10)
        self.speed(10)
        self.Pen_Color = ['Red', "Black", "Blue", "Yellow", "Green"]
        In_Pix = list(map(int, input("X, Y, r:?").split()))

        try:
            self.x_pos, self.y_pos, self.Cir_r = In_Pix
        except:
            try:
                self.x_pos, self.y_pos = In_Pix
            except:
                try:
                    if In_Pix[0] is not None: self.x_pos = In_Pix[0]
                except:
                    self.x_pos = 100
                self.y_pos = 100
            self.Cir_r = 100
        print(self.x_pos, self.y_pos, self.Cir_r)
        pass

    def Circle5(self):
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        move_range = (self.Cir_r*2)*0.7

        for i in range(3):
            self.pencolor(self.Pen_Color[i])
            self.pendown()
            self.circle(self.Cir_r)
            self.penup()
            print(self.xcor())
            self.setx(self.xcor()-move_range)
            pass
        
        self.goto(self.xcor()+move_range/2, self.ycor()-move_range)
        for i in range(2):
            self.pencolor(self.Pen_Color[i+3])
            self.setx(self.xcor()+move_range)
            self.pendown()
            self.circle(self.Cir_r)
            self.penup()
            print(self.xcor())
            pass
        pass

if __name__ == "__main__":
    MyTurtle = My_Turtle()
    MyTurtle.Circle5()