# Author: Lilbox
# Time:2022/1/11 11:05


lis=[4,2,2,4]
val=4
i=0
j=1
num=len(lis)
c=0
if not lis:#空
    print(0)
else:
        lis.insert(0,'*')
       #i j指向初始位置
        while lis[j]!=val and j<num:#j指向被删元素列表的首位
             j+=1
             i=j-1
        else:
            while j<=num:
                 if lis[j]==val:
                    j+=1
                 else:
                     i += 1
                     lis[i] = lis[j]
                     j += 1
        print(lis)
        print(i)
#     i=c=0
#     num=len(lis)
#     j=num-1
#     while lis[j]==val and j>0:
#                j-=1
#     if j==0:
#         print(0)
#
#     while i<j:#只要满足i！=j就一直执行
#          if lis[i]==val and j>0:
#                 c=lis[i]
#                 lis[i]=lis[j]
#                 lis[j]=c
#                 i+=1
#                 j-=1
#          else:
#               i+=1
#     print(j+1)

# def removeElement(lis:list[int],val:int):
#     num=len(lis)
#     if num==
