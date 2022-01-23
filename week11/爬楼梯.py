# Author: Lilbox
# Time:2022/1/17 10:43
import math

n=1


i=n-1
j=1
sum=1
while i>=(n/2):
     sum+=(math.factorial(i))//((math.factorial(j))*math.factorial((i-j)))
     i-=1
     j+=1
print(sum)