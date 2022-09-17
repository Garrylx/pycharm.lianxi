"""author = "GARRY GY"
Date:2021-07-13
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
# 移动柱子
#相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)的游戏。该游戏是在一块铜板装置上，
#有三根杆(编号A、B、C)，在A杆自下而上、由大到小按顺序放置64个金盘(如图1)。游戏的目标：
#把A杆上的金盘全部移到C杆上，并仍保持原有顺序叠好。操作规则：每次只能移动一个盘子，
# 并且在移动过程中三根杆上都始终保持大盘在下，小盘在上，操作过程中盘子可以置于A、B、C任一杆上

# 分为三步解决
#以C盘为中介，从A杆将1至n-1号[作为整体]盘移至B杆；
#将A杆中剩下的第n号盘移至C杆；
#以A杆为中介；从B杆将1至n-1号盘移至C杆

def Hanoi(n,a,b,c):
    if  n > 0:
        Hanoi(n-1,a,c,b)

        print("moving from %s to %s" % (a,c))

        Hanoi(n-1,b,a,c)

Hanoi(4,"a","b","c")
