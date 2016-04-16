#coding=utf-8
from __future__ import print_function    #引入python3的print语法

nmp = [[0 for col in range(20)]
      for row in range(20)]
mp = [[0 for col in range(20)]
      for row in range(20)]

def update(n, x, y):
    _dir = [[-2,-2],[-1,-1],[1,1],[2,2],
           [1,-1],[2,-2],[-1,1],[-2,2]]
    for i in range(8):
        if (x+_dir[i][0]>= 1) and (x+_dir[i][0]<=n) and (y+_dir[i][1]>=1) and (y+_dir[i][1]<=n):
            nmp[x+_dir[i][0]][y+_dir[i][1]] += 1

num = int(raw_input())
for i in xrange(num):
    col = int(raw_input())
    for x in xrange(col):
        strt = str(raw_input())
        for y in xrange(col):
            mp[x][y] = strt[y]
            if mp[x][y] == "x":
                update(col, x, y)
    for p in xrange(col):
        for q in xrange(col):
            if mp[p][q] == "x":
                print("x", end="")
            else:
                print(nmp[p][q], end="")
        print("\r")
    
