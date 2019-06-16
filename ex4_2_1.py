import turtle

pen = turtle.Turtle()

# 定义单片花瓣的绘制函数
def pedal(r, d):
    pen.circle(r, d)
    pen.lt(180 - d)
    pen.circle(r, d)
    
radius = int(input('r:')) # 花瓣的半径
degree = int(input('d:')) # 花瓣的弧度
pedal(radius, degree)
