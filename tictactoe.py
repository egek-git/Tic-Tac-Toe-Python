import turtle
import random
#Screen
screen = turtle.Screen()
screen.title("TicTacToe")
screen.bgcolor("#648CB9")
screen.setup(width=420, height=420)
#text
text = turtle.Turtle()
text.penup()
text.speed(0)
text.hideturtle()
text.color("Red")
#Grid
grid = turtle.Turtle()
grid.color("#365378")
grid.speed(0)
for x in range(-210,210,140):
    grid.penup()
    grid.goto(x,210)
    grid.pendown()
    grid.goto(x,-210)
for y in range(-210,210,140):
    grid.penup()
    grid.goto(210,y)
    grid.pendown()
    grid.goto(-210,y)
boxes = {
    "upper_left": (-140, 140),
    "upper_middle": (0, 140),
    "upper_right": (140, 140),
    "middle_left": (-140, 0),
    "middle_middle": (0, 0),
    "middle_right": (140, 0),
    "bottom_left": (-140, -140),
    "bottom_middle": (0, -140),
    "bottom_right": (140, -140)
}
written = {
    "upper_left": "",
    "upper_middle": "",
    "upper_right": "",
    "middle_left": "",
    "middle_middle": "",
    "middle_right": "",
    "bottom_left": "",
    "bottom_middle": "",
    "bottom_right": ""
}
win = [
    ["upper_left","upper_middle","upper_right"],
    ["middle_left","middle_middle","middle_right"],
    ["bottom_left","bottom_middle","bottom_right"],
    ["upper_left","middle_left","bottom_left"],
    ["upper_middle","middle_middle","bottom_middle"],
    ["upper_right","middle_right","bottom_right"],
    ["upper_left","middle_middle","bottom_right"],
    ["upper_right","middle_middle","bottom_left"]
]
emptyboxes = list(boxes.keys())
# x = player
player = turtle.Turtle()
player.penup()
player.hideturtle()
def gotobox(box):
    coordinate = boxes[box]
    x = coordinate[0]
    y = coordinate[1]
    player.goto(x, y-55)
def writeO():
    a = random.choice(emptyboxes)
    emptyboxes.remove(a)
    gotobox(a)
    player.write("O", align="center", font=("Arial", 75, "bold"))
    written[a] = "O"
    check()
def click_function(x,y):
    for box_name, coordinate in boxes.items():
        x_center = coordinate[0]
        y_center = coordinate[1]
        if (x_center -70 < x < x_center +70) and (y_center -70 < y < y_center +70):
            # box_name is hit
            if box_name in emptyboxes:
                gotobox(box_name)
                player.write("X", align="center", font=("Arial", 75, "bold"))
                emptyboxes.remove(box_name)
                written[box_name] = "X"
                if check():
                    return
                writeO()
            break
def check():
    for situation in win:
        box1 = situation[0]
        box2 = situation[1]
        box3 = situation[2]
        if written[box1] == written[box2] == written[box3] and written[box1] != "":
            print(f"GAME OVER! WINNER: {written[box1]}")
            if written[box1] == "X":
                text.write("You Win!", align="center", font=("Arial", 35, "bold"))
            else:
                text.write("You Lose!", align="center", font=("Arial", 35, "bold"))
            screen.exitonclick()
            return True        
    if len(emptyboxes) == 0:
        print("Draw!")
        text.write("It's a Draw!", align="center", font=("Arial", 35, "bold"))
        screen.exitonclick()
        return True 
    return False
screen.onscreenclick(click_function)
screen.mainloop()