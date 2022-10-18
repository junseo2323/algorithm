a,b,c = map(int,input().split())

tmp = c-b

print(a//tmp+1 if c-b > 0 else -1)
