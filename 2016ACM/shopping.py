#coding=utf-8

fd = [0 for i in xrange(10086)]   #初始化一维，通用模板数组
nfd = [0 for i in xrange(10086)]

T = int(raw_input())
for i in range(T):
    _sum = 0.0
    posf = 0
    posn = 0
    n,m = map(int, raw_input().split())
    for x in range(m):
        p,t = map(int, raw_input().split())
        p = float(p)
        if t == 1:
            fd[posf] = p*0.8
            posf += 1
            _sum += p*0.8
        else:
            nfd[posn] = p
            posn += 1
            _sum += p
    fd.sort(reverse=True)    #排序，加上reverse=True表示按降序排列
    nfd.sort(reverse=True)
    lenf = posf
    lenn = posn
    posf = posn = 0
    for q in range(n):
        if posn == lenn:
            break
        if q == n-1:
            if posf == lenf:
                _sum -= nfd[lenn-1]/2.0
            else:
                _sum -= min(nfd[lenn-1], fd[lenf-1])/2.0
        else:
            _sum -= nfd[posn]/2.0
            posn += 1
    print "%.2f\r" % _sum 
    
            



