from turtle import Turtle, Screen
from random import choice, randint



screen = Screen()
screen.title("Welcome to Turtle Race!")
screen.bgcolor('#ffffff')
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ').lower()
# print(user_bet)



finish_line = Turtle()
finish_line.penup()
finish_line.goto(x=235, y=195)
finish_line.pendown()
finish_line.goto(x=235, y=-185)
finish_line.hideturtle()


colors = ['purple', 'blue', 'orange', 'red', 'gold', 'green']



def turtle_factory():
    nts_list = [] # ninja turtles list
    '''Creates turtles and gives them a color'''
    y = -165
    used_colors = []
    
    for i in range(len(colors)):
        tmnts = Turtle(shape='turtle') # teenage mutant ninja turtles
        tmnts.penup()
        tmnts.goto(x=-235, y=y)
        
        tmnts.color(choice(colors))
        used_colors.append(tmnts.pencolor())

        if tmnts.pencolor() in used_colors:
            colors.remove(tmnts.pencolor())

        nts_list.append(tmnts)
        y += 65 # add spacing
    return nts_list

nts = turtle_factory()



def turtles_run():
    '''Prompts turtles to start the race'''
    for nt in nts:
        if nt.xcor() > finish_line.xcor():
            winner = Turtle()
            winner.penup()
            winner.hideturtle()
            winner.color(nt.pencolor())
            winner.write('The winner is ' + nt.pencolor(), align='center', font=('Arial', 25))

            winner.goto(x=0, y=-25)
            if user_bet == nt.pencolor():
                winner.write("You've guessed right!", align='center', font=('Arial', 15))
            else:
                winner.write("Incorrect guess. Try again!", align='center', font=('Arial', 15))

            return nt.pencolor() # returns winning color(s)
        else:
            nt.forward(randint(0, 25)) # lower the range the greater chance of a stackoverflow
    
    turtles_run() # recursive function
turtles_run()



screen.exitonclick()