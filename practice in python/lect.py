f = open('C:\\Users\\Kushal Tripathi\\python\\practice in python\\demoFile.txt', 'r')
data =f.read()
print(data)

line1 =f.readline(1)


print(line1)
line2=f.read(3)
print(line2)

f.close()