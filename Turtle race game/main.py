import turtle, random

sim = turtle.Screen()
# is_race_going=True
sim.setup(500, 400)
colors = ["red", "blue", "violet", "green", "orange"]
list1 = [0, 35, 70, -35, -70]
list_turtle = []
user_bet = sim.textinput(title="Make your bet", prompt="Which turtle will win the race?Guess the colour")

for i in range(0, 5):
    tim = turtle.Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-240, y=list1[i])
    list_turtle.append(tim)

is_race_going = True

while is_race_going:
    for turtle in list_turtle:
        a = random.randint(0, 9)
        turtle.forward(a)
        if turtle.xcor() > 230:
            print(turtle.color())
            is_race_going = False
            if turtle.color()[0] == user_bet:
                print("Congratulations ! You won")

            else:
                print("Ohhh! Nooooo")
            break

sim.exitonclick()
