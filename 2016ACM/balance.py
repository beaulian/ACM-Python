num = int(raw_input())
data = map(int, raw_input().split())
balance = 0;
for i in data:
    if i % 2 == 1:
        balance -= 1
    else:
        balance += 1
if balance == 0:
    print "B"
else:
    print "U"
