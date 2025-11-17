import numpy as np
f=open('input.txt')
o=open('output.txt','w')
a=len(f.readlines())
f.seek(0)
n=int(f.readline().strip())
d={}
for i in range(n):
    s=f.readline().strip().split()
    d[s[0]]=int(s[1])
e={}
for i in range(a-n-1):
    s=f.readline().strip()
    e[s]=e.get(s,0)+1
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
j={}
print(b,d,e, sep="\n")
for i in range(len(d)):
    print(len(d))
    j[sorted(d)[i]]=sorted(b[i],key=lambda x:b[i][x])[len(d)-1]
    print(j)
    print(str(j[sorted(d)[i]])+" "+str(d[sorted(d)[i]]),file=o)