from turtle import Turtle, Screen


'''
w = forwards
s = backwards
a = counter-clockwise
d = clockwise
c = clear drawing
'''

tim = Turtle()
screen = Screen()
screen.title('etch_a_sketch')

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def reset_screen():
    tim.reset()
    

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=reset_screen)





screen.exitonclick()