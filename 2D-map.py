#import 
from random import randint 
from numpy import zeros
from time import localtime, strftime ,sleep
from datetime import datetime
import os
import sys
from PIL import Image

start = datetime.now()

#可以改的兩個參數
x = 100
count = 1000000

#隨機生成x*x的亂數陣列
map1 = zeros((x,x),dtype = int)
for i in range(x):
    for j in range(x):
            map1[i][j] = randint(0,3)
#0 海洋 藍色
#1 草地 淺綠
#2 沙漠 黃色
#3 樹林 深綠


#隨機挑選一個點 使那個點周圍與那個點數字相同 直到count=0結束
#      2                          0
#    1 0 1      =====>          0 0 0
#      3                          0

while count != 0:
    rd_x = randint(1,x-2)
    rd_y = randint(1,x-2)
    map1[rd_x-1][rd_y],map1[rd_x][rd_y-1], map1[rd_x+1][rd_y] , map1[rd_x][rd_y+1] = map1[rd_x][rd_y] , map1[rd_x][rd_y] , map1[rd_x][rd_y], map1[rd_x][rd_y]    
    count = count - 1


#尋找一個點 如果那個點周圍數字與那個點不同 把周圍數字變成那個點
#        1                          1
#      1 0 1        ======>       1 1 1
#        1                          1

for i in range(1,x-1):
    for j in range(1,x-1):
        if map1[i-1][j] != map1[i][j] and map1[i][j-1] != map1[i][j] and map1[i+1][j] != map1[i][j] and map1[i][j+1] != map1[i][j]:
            map1[i][j] = map1[i-1][j]
#邊邊狀況
#     1                         1
#     0 1         ======>       1 1
#     1                         1

for i in range(1,x-1):
    if map1[0][i] != map1[1][i] and map1[0][i] != map1[0][i-1] and map1[0][i] != map1[0][i+1]:
        map1[0][i] = map1[1][i] 
    if map1[x-1][i] != map1[x-2][i] and map1[x-1][i] != map1[x-1][i-1] and map1[x-1][i] != map1[x-1][i+1]:
        map1[x-1][i] = map1[x-2][i]
    if map1[i][0] != map1[i][1] and map1[i][0] != map1[i+1][0] and map1[i][0] != map1[i-1][0]:
        map1[i][0] = map1[i][1] 
    if map1[i][x-1] != map1[i][x-2] and map1[i][x-1] != map1[i+1][x-1] and map1[i][x-1] != map1[i-1][x-1]:
        map1[i][x-1] = map1[i][x-2]

#角落狀況
#     0 1                     1 1
#     1         ======>       1 

if map1[0][0] != map1[0][1] and map1[0][0] != map1[1][0]:
    map1[0][0] = map1[0][1]
if map1[0][x-1] != map1[0][x-2] and map1[0][x-1] != map1[1][x-1]:
    map1[0][x-1] = map1[0][x-2]
if map1[x-1][0] != map1[x-1][1] and map1[x-1][0] != map1[x-2][0]:
    map1[x-1][0] = map1[x-1][1]
if map1[x-1][x-1] != map1[x-1][x-2] and map1[x-1][x-1] != map1[x-2][x-1]:
    map1[x-1][x-1] = map1[x-2][x-1]


#抓取路徑

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

file_tree = "color\\tree.png"
file_ocean = "color\\ocean.png"
file_desert = "color\\desert.png"
file_grass = "color\\grass.png"




#圖片套入

map2 = Image.new( "RGB", (16 * x,16 * x) )
tree = Image.open(resource_path(file_tree))
ocean = Image.open(resource_path(file_ocean))
desert = Image.open(resource_path(file_desert))
grass = Image.open(resource_path(file_grass))

for i in range(x):
    for j in range(x):
        if map1[i][j] == 0:
            map2.paste( ocean, (16 * j, 16 * i) )   
        if map1[i][j] == 1:
            map2.paste( grass, (16 * j, 16 * i) )
        if map1[i][j] == 2:
            map2.paste( desert, (16 * j, 16 * i) )
        if map1[i][j] == 3:
            map2.paste( tree, (16 * j, 16 * i) )

#圖片匯出
t = localtime()
time_ = strftime("%Y-%m-%d %H-%M-%S", t)
map2.save("map {0} .png".format(time_))

#print 執行時間
end = datetime.now()
print("執行時間：", end - start)
os.system("pause")
