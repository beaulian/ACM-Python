num = int(raw_input())
for i in xrange(num):
    data = map(int, raw_input().split())
    data[0] -= data[2]
    while data[0] > 0:
        exp = 300+(data[1]-1)*100
        data[0] -= exp
        data[1] -= 1
    currlv =  -data[0]
    print data[1], currlv
