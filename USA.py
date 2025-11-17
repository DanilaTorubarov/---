import numpy as np
f=open('input.txt')
f1=open('output.txt','w')
a=len(f.readlines())
f.seek(0)
n=int(f.readline().strip())
d={}
for i in range(n):
    s=f.readline().strip().split()
    d[s[0]]=int(s[1])
print(d)
e={}
for i in range(a-n-1):
    s=f.readline().strip()
    e[s]=e.get(s,0)+1
print(e)
b=[]
for i in range(n):
    b.append({})
g=sorted(e)
s0=(g[0].split())[0]
h=0
for i in g:
    if s0!=i.split()[0]:
        h+=1
        s0=i.split()[0]
    b[h][i.split()[1]]=e[i]
print(b)
j={}

for i in range(len(d)):
    j[sorted(d)[i]]=sorted(b[i])
