st='mithunIsAGoodBoy'
le=list(st)
res=''
print(le)
for i in le:
    if i<='Z' and i>='A':
        res+='_'+i.lower()
    else:
        res+=i

print(res)