from collections import Counter 
x = int(input())
y = input()
a = [ int(num) for num in y.split() ]
e = Counter(a)
N = int(input())
key_count=0
for i in range(N):
        o = input()
        p =[ int(f) for f in o.split()] 
        if e[p[0]]:
            key_count += p[1]
            e[p[0]] -= 1   
print(key_count)