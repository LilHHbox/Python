# Author: Lilbox
# Time:2022/1/14 18:13


s = "Hel"
length=len(s)
i=len(s)-1
c=0
while i>0:
    if s[i]!=' ':
         k=i
         j=i
         while j>=0:
             if s[j]==' ':
                 print(k-j)
                 break
             else:
                 j-=1
         break
    else:
        i-=1
print(i+1)


