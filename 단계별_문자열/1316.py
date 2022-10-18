def check_group(x) :
    x = list(x)
    
    for i in range(len(x)):
        try :
            if x[i] == x[i+1] :
                x[i] = 0
        except IndexError :
            continue

    for i in x:
        if i!=0 :
            if x.count(i) > 1 :
                return False
            else :
                continue
    return True

a = int(input())
cnt = 0
for i in range(a):
    b = input()
    if check_group(b) :
        cnt += 1
print(cnt)
