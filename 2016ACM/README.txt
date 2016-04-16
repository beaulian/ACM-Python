输入单个数据

python使用raw_input接收用户的输入，但不会判断类型，所以必须在赋值之前转换类型，如s = int(raw_input())
输入一行数据

oj题目经常会有1 2 3 4这样的输入，如果直接用上面的raw_input会显得比较麻烦，还要自己用split函数解析
python提供了一个强大的函数map，可以很轻松地解决这个问题
data = map(int, raw_input().split())，int指代输入类型，其他的不用管，data直接是一个输入数据列表
但是对1234这种无能为力，但是可以这样，先用s = str(raw_input())获得“1234”字符串，再遍历这个字符串
for i in s:
   data.append(int(s))

输出
python2有个不好的地方就是print很蛋疼，默认换行，print "n"直接给你换行了，如果想输出12345这样紧挨的数据
以C语言为例
int data[4] = {1,2,3,4};
int i；
for (i=0; i<4; i++) printf("%d", data[i]);
可以输出1234，但是python呢 
for i in data:
  print i
输出的是
1
2
3
4
可能会有人这样做
for i in data:
  print i,
在print后面加个逗号可以不换行，但是输出的是这样的
1 2 3 4
也不是我们想要的输出
这个时候就要想到python3了，python3的print比较好，可以指定输出的结尾是什么
for i in data:
  print(i, end="")
这样就行了，但是我们是在python2的环境下，怎么办，有人早就想到了
python内置了__future__模块，里面有很多python3的功能，其中也包括print函数
from __future__ import print_function
在开头加一句这个，文件里面的print就变成python3的print了

还有一个就是print "\n"后会多一行空格，有时候不符合题意，可以这样print "\r"
