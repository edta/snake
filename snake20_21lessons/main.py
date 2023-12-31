import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
from wall import Wall

screen = Screen()

screen.setup(width= 600, height=600)
screen.bgcolor("gray")
answer = screen.textinput("", "Are you Maga? Type yes or no")
if answer == 'yes':
    screen.bgpic("flag.gif")
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(snake.up , "w")
screen.onkey(snake.down , "s")
screen.onkey(snake.right , "d")
screen.onkey(snake.left , "a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_snake()

    # Detect collision with wall
    if (snake.head.xcor() > 260 or snake.head.xcor() < -260 or
            snake.head.ycor() > 275 or snake.head.ycor() < -270):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with body
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    snake.move()

screen.exitonclick()