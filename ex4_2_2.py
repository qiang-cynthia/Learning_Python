import turtle

pen = turtle.Turtle()

def pedal(r, d):
    '''单个花瓣的绘制函数，注意反向线条的角度处理'''
    pen.circle(r, d)
    pen.lt(180 - d)
    pen.circle(r, d)
    
radius = int(input('r:')) # 花瓣的半径
degree = int(input('d:')) # 花瓣的弧度
num = int(input('petals:')) # 花瓣的片数

for i in range(num):
    '''每画完一个花瓣，就让鼠标回到原始状态，绘制下个花瓣就只要考虑采用花瓣序号对起始角度进行偏置就行了'''
    pedal(radius, degree)
    pen.home()
    pen.rt((i + 1) * 360 / num)
