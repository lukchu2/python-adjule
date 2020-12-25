p,k= map(int, input().split())
t=input()
t=int(t)
if p <= t <= k:
    print('BINGO')
else:
    if t<p:
        print(p-t)
    else:
        print(t-k)