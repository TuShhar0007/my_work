""" one liner answer for following question
print("".join(sorted(list(input()),key= lambda x : (-x.islower() ,-x.isupper(), int(x) % 2 == 0 if x.isdigit() else None,x)))) """
# ginorts problem qeustion hacker rank

s = input()
c = list(s)
d = []
l = [] 
n = []
t = []
e= []
for i in c:
    if i.islower()== True:
        l.append(i)
for a in c:
       if a.isupper()==True:
           n.append(a)
for b in c:
    if b.isnumeric()==True:
        if int(b)%2!=0:
            t.append(b)
m = [e.append(h) for h in c if h not in t and h.isnumeric()==True]
w = (sorted(l)+sorted(n)+sorted(t)+sorted(e))
print("".join(w))


