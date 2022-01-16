# Author: Lilbox
# Time:2022/1/14 20:45


digits = [3,9,9]




i=len(digits)-1
while i>=0:
    if digits[i]!=9:
        digits[i]+=1
        break
    else:
        digits[i]=0
        i-=1

for j in digits:
    print(j)
