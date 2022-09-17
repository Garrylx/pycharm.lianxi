"""shape = [tr1,
         sw1,
         cr1]
for a_shape in shape:
    a_shape.draw()"""


class drawing:
    def __init__(self,cir1,tri1,rec1):
        self.circle= cir1
        self.triangle = tri1
        self.recq = rec1

    def draw_rectangle(self):
        print('gy正在画矩形{}'.format(self.rectangle))
        import turtle
        rec1 = turtle.Turtle()
        chang = int(input('请输入长度'))
        kuan = int(input('请输入宽度'))
        p = input('请输入颜色')
        rec1.pencolor(p)
        rec1.fd(chang)
        rec1.lt(90)  # 左转90度
        rec1.fd(kuan)  # 移动100距离
        rec1.lt(90)
        rec1.fd(chang)
        rec1.lt(90)
        rec1.fd(kuan)
        print(rec1)
        turtle.mainloop()  # 给用户展示窗口
    def draw_circle(self):
        print("gy正在画圆形{}".format(self.circle))
        import turtle
        import math
        r = int(input('请输入圆的半径'))
        p = input('请输入颜色')
        circum = 2 *math.pi*r
        n = 50
        step1 = circum//50
        angle = 360/n
        cir1 = turtle.Turtle()
        cir1.pencolor(p)
        for i in range(n):
            cir1.fd(step1)
            cir1.lt(angle)
        print(cir1)
        turtle.mainloop()
    def draw_triangle(self):
        print("gy正在画三角形{}".format(self.triangle))
        """l1 = int(input("请输入第一条边"))
        l2 = int(input('请输入第二条边'))
        l3 = int(input('请输入第三条边'))
        while l1+l2 <= l3 or l2+l3 <= l1 or l1+l3 <=l2:
            print("不能组成三角形哦，请再次输入")
            l1 = int(input("请输入第一条边"))
            l2 = int(input('请输入第二条边'))
            l3 = int(input('请输入第三条边'))"""#任意好难
        print('只能画等边哦')
        longs = int(input('请输入边长'))
        p = input('请输入颜色')
        import turtle
        tri1 = turtle.Turtle()
        tri1.pencolor(p)
        for i in range(3):
            tri1.fd(longs)
            tri1.lt(120)
        print(tri1)
        turtle.mainloop()




gydw1 = input('请输入一个圆形名称')
gydw2 = input('请输入一个三角形名称')
gydw3 = input('请输入一个矩形名称')
draw1 = drawing(gydw1,gydw2,gydw3)
huatu = input('请输入"draw_circle"或"draw_triangle"或"draw_rectangle"')
if huatu == "draw_circle":
    draw1.draw_circle()
elif huatu == "draw_triangle":
    draw1.draw_triangle()
else:
    draw1.draw_rectangle()





