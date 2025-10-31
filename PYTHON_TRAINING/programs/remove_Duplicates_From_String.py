st=input("enter string")
st2=""
for j in range(0,len(st)):
    if st[j] in st2 :
        continue
    st2 += st[j]

print(st2)


