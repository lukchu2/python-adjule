x, y = map(int, input().split())
n = input()
n = int(n)
t=[int(s) for s in input().split()]
pk=0
i=0
for i in range(n):
    if x<=t[i]<=y:
        pk=0
    elif t[i]<x:
        pk+=x-t[i]
    else:
        pk+=t[i]-y
print (pk)

LUB


x, y = map(int, input().split())
n = input()
n = int(n)
t=[int(s) for s in input().split()]
t1=[]
pk=0
i=0
for i in range(0,n):
    t1.append(t[i])
    t1[i]=int(t1[i])
i=0
for i in range(n):
    if x<=t1[i]<=y:
        pk=0
    elif t1[i]<x:
        pk+=x-t[i]
    else:
        pk+=t1[i]-y
print (pk)
