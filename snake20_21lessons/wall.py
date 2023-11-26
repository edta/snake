from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segment_list = []
        self.create_tb_wall(290)
        self.create_tb_wall(-285)
        self.create_rl_wall(280)
        self.create_rl_wall(-295)


    def create_tb_wall(self, y_cor):
        for i in range(-300, 300, 20):
            segment = Turtle('circle')
            self.segment_list.append(segment)
            segment.color('green')
            segment.penup()
            segment.goto(i, y_cor)

    def create_rl_wall(self, x_cor):
        for i in range(-300, 300, 20):
            segment = Turtle('circle')
            self.segment_list.append(segment)
            segment.color('green')
            segment.penup()
            segment.goto(x_cor, i)

