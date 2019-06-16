import turtle
from math import cos, pi

pen = turtle.Turtle()
radius = int(input('radius:'))
sides = int(input('sides:'))
angle = (180 - 360.0 / sides) / 2 # 三角形单元的底角度数

def side_length(r, d):
    value = abs(2 * r * cos(d / 180.0 * pi))
    return round(value)
    
def triangle(r, d):
    pen.fd(r)
    pen.rt(180 - d)
    pen.fd(side_length(r, d))
    pen.rt(180 - d)
    pen.fd(r)
    
for i in range(sides):
    triangle(radius, angle)
    pen.home()
    # 相邻的下一个三角形单元的偏置角度
    pen.rt(360 / sides * (i + 1)) 
