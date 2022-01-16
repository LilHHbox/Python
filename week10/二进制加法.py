# Author: Lilbox
# Time:2022/1/15 17:46


#列表转化为字符串

# lis=['1','2']


# lis=[1,2,3]
# str=''.join(str(e) for e in lis)
# print(str)



a='100'
b='101'
lisa=[]
lisb=[]
lisc=[]
lengtha=len(a)
lengthb=len(b)
for i in range(lengtha):
    lisa.append(a[i])
for j in range(lengthb):
    lisb.append(b[j])
l=max(lengtha,lengthb)
if lengtha<l:
    for i in range(l-lengtha):
        lisa.insert(i,'0')
elif lengthb<l:
    for i in range(l-lengthb):
        lisb.insert(i,'0')
l-=1
count='0'
while l>=0:
    if lisa[l]==lisb[l]=='1':
        if count=='1':
            lisc.insert(0, '1')
        else:
            lisc.insert(0,'0')
            count='1'
        l-=1
    elif lisa[l]==lisb[l]=='0':
        if count=='1':
            lisc.insert(0,'1')
            count='0'
        else:
            lisc.insert(0,'0')

        l-=1
    else:
        if count=='1':
            lisc.insert(0,'0')
        else:
            lisc.insert(0,'1')
        l-=1
if count=='1':
    lisc.insert(0,'1')


str=''.join(lisc)
return str



print(str)