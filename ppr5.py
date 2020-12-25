p,k=map(int,input().split())
d=input()
if "o"<d<"r":
    if p%2==0:
        while p<=k:
          print(p)
          p=p+2
    else:
        p=p+1
        while p<=k:
          print(p)
          p=p+2
if "m"<d<"o":
    if p % 2 == 0:
        p = p + 1
        while p <= k:
            print(p)
            p = p + 2
    else:
        while p <= k:
            print(p)
            p = p + 2