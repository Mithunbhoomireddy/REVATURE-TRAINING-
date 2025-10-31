st='mithun'
li={}
for i in range(len(st)):
    for j in range(len(st)-1-i,-1,-1):
        li[i]=st[j]
        break
res="".join(li.values())
print(res)