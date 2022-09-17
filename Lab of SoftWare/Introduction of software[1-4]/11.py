"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
num = int(input("Enter a integer: "))
file = input("Enter a filename: ")
xfile = open(file,"r")
count = 0
file_read = xfile.read()
for x in file_read:
    if x % num == 0:
        count += 1
    else:
        pass
print("There is " + str(count) + " multiple of " + str(num) + " in the " + file + " file.")
count = 0
xfile.close()


i = int(input('Enter an integer: '))
file = input('Enter a filename: ')
fp = open(file,'r')
text = fp.read().split()
text = list(map(int,text))

count = 0
for j in text :
	if j%i == 0:
		count += 1
if count == 1:
	print("There is 1 multiple of {} in the '{}' file.".format(i,file))
else:
	print("There are {} multiples of {} in the '{}' file.".format(count,i,file))

fp.close()
