import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dense Red Flowers with Stems and Star Rain")
screen.setup(width=1000, height=700)
screen.tracer(0)


def draw_flower(t, radius, color):
    t.color(color)
    t.begin_fill()
    for _ in range(12):
        t.circle(radius, 60)
        t.left(150)
    t.end_fill()


def draw_stem(t, start_x, start_y):
    t.color("green")
    t.pensize(4)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.goto(start_x, start_y - 100)
    t.penup()


def draw_leaf(t, x, y):
    t.color("darkgreen")
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.circle(20, 90)
    t.left(90)
    t.circle(20, 90)
    t.end_fill()
    t.penup()


stars = []
for _ in range(40):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.penup()
    star.speed(0)
    star.shapesize(0.4, 0.4)
    star.goto(random.randint(-490, 490), random.randint(150, 350))
    stars.append(star)


positions = []
start_x = -300
end_x = 300
step_x = 70
base_y = -270
rows = 4
row_height = 25

for row in range(rows):
    y = base_y + row * row_height
    for x in range(start_x, end_x + 1, step_x):
        rand_x = x + random.randint(-15, 15)  # X'e küçük sapma
        rand_y = y + random.randint(-10, 10)  # Y'e küçük sapma
        positions.append((rand_x, rand_y))


red_colors = ["red", "darkred", "firebrick", "crimson", "indianred"]

flowers = []
stems = []
leaves = []

for pos in positions:
    x, y = pos
    stem = turtle.Turtle()
    stem.hideturtle()
    stem.speed(0)
    draw_stem(stem, x, y)
    stems.append(stem)

for pos in positions:
    x, y = pos
    leaf = turtle.Turtle()
    leaf.hideturtle()
    leaf.speed(0)
    draw_leaf(leaf, x, y - 80)
    leaves.append(leaf)

for pos in positions:
    flower = turtle.Turtle()
    flower.hideturtle()
    flower.speed(0)
    flower.penup()
    flower.goto(pos)
    flowers.append(flower)

max_radius = 40
growth_speed = 1
current_radii = [0] * len(flowers)

while True:
    for star in stars:
        x, y = star.pos()
        if y < -350:
            star.goto(random.randint(-490, 490), random.randint(200, 350))
        else:
            star.sety(y - random.randint(4, 7))

    for i, flower in enumerate(flowers):
        if current_radii[i] < max_radius:
            current_radii[i] += growth_speed
            flower.clear()
            flower.showturtle()
            draw_flower(flower, current_radii[i], random.choice(red_colors))
        else:
            draw_flower(flower, max_radius, random.choice(red_colors))

    screen.update()
    time.sleep(0.03)
