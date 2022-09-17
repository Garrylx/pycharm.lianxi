
#[MFTOLP]-2020S-Exam-n乘n矩阵连通区域判定
def eight(array,center,r,c,n,count):#定义函数eight
    # array  作为输入数组，同时在后续计算中，存储count
    # center 作为标记数组
    # r 列
    # c 行
    # n 方阵大小
    # count 计数器

    #以下部分代码的功能是：
    if array[r][c] != 0 and center[r][c] == 1:
       #如果array[r][c]（array的第r行第c列）不等于0且center[r][c]等于1
       #那么先进行如下操作
       array[r][c] = count#将array[r][c]赋值为count（把当前array[r][c]存储的值更新）
       center[r][c] = 0#将center[r][c]赋值为0（将此位置标记为已操作)
       #再进行递归
    else:
       return#否则终止递归
    if r==0:#如果r==0
        #也就是最左一列
        if c==0:#且c==0
            #此时运算到了最左上角
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c+1,n,count)#向下一行、下一列递归
        elif c==n-1:
            #此时运算到了左下角
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c-1,n,count)#向上一行、下一列递归
        else:
            #此时运算到了最左一列
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r+1,c-1,n,count)#向上一行、下一列递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c+1,n,count)#向下一行、下一列递归
    elif r==n-1:#如果r==n-1
        #也就是最右一列
        if c==0:#且c==0
            #也就是右上角
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c+1,n,count)#向上一列，下一行递归
        elif c==n-1:#右下角
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c-1,n,count)#向上一行、上一列递归
        else:
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r-1,c-1,n,count)#向上一行、上一列递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c+1,n,count)#向上一列，下一行递归
    else:#列不在两边
        if c==0:#最上行
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c+1,n,count)#向上一列，下一行递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c+1,n,count)#向下一行、下一列递归
        elif c==n-1:#最下行
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c-1,n,count)#向上一行、上一列递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c-1,n,count)#向上一行、下一列递归
        else:#现在array[r][c]不在边角上，任何方向都可以走，所以八个方向都可以走
            eight(array,center,r,c-1,n,count)#向上一行递归
            eight(array,center,r,c+1,n,count)#向下一行递归
            eight(array,center,r-1,c-1,n,count)#向上一行、上一列递归
            eight(array,center,r-1,c,n,count)#向上一列递归
            eight(array,center,r-1,c+1,n,count)#向上一列，下一行递归
            eight(array,center,r+1,c-1,n,count)#向上一行、下一列递归
            eight(array,center,r+1,c,n,count)#向下一列递归
            eight(array,center,r+1,c+1,n,count)#向下一行、下一列递归


#以下部分代码的功能是：声明与输入
n = int(input())#输入方阵大小n
array = list()#声明列表
for r in range(n):#循环n次
   a=[int(c) for c in input().split()]#声明列表，同时让用户输入；
   #输入之后，用split切割，存储到array里
   array.append(a)#存储

center = list()#声明列表center
for r in range(n):#循环n次
    a = list()#声明列表
    for c in range(n):#循环n次
        a.append(1)#列表a添加元素：1
    center.append(a)#列表center添加元素：列表a
#此时center为一个全为1的列表
#此时array是输入进来的那个列表
#可以把下面的debug代码删掉看一下
#print(array)
#print(center)
#
#
#
#

#以下部分代码的功能是：计算
count = 0#声明计数器， count
for r in range(n):#外层循环n次
    for c in range(n):#内层循环n次
        if array[r][c] != 0:#如果array[r][c]不等于0
            if center[r][c]==1:#且array[r][c]等于1
               count = count + 1#计数
               eight(array,center,r,c,n,count)#调用函数
        else:#等于0的话，就把center[r][c]赋值为0
            center[r][c] = 0
#print(array)
#print(center)
#
#
#
#

#以下部分代码的功能是：取array中的最大数值，存储到count中
count = 0#计数器重新记为0
for r in range(n):#循环n次
    for c in range(n):#内层循环n次
        if array[r][c]>count:#如果array[r][c]大于计数器
            count = array[r][c]#把array存到计数器里
#
#
#
#

#以下部分代码的功能是：输出count
print(count)