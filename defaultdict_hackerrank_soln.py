from collections import defaultdict
x = input()
c = [ n for n in x if n!=" "]
d =defaultdict(list)
for i in range(int(c[0])):
    n = input()
    d[n].append(i+1)
for k in range(int(c[1])):
    m = input()
    if m in d:
        print(*d[m])
    else:
        print(-1)
