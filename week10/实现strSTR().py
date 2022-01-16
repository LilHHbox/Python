# Author: Lilbox
# Time:2022/1/12 12:41

#暴力解法会超时
# str0='poiu'
# str1='oi'
# len0=len(str0)
# len1=len(str1)
# i=0
# j=0
# if str1 not in str0 :
#     print(-1)
# elif len1==0:
#     print(0)
# for i in range(len0-len1):
#     if str0[i]!=str1[0]:#确定i的位置
#         i+=1
#     elif str0[i+len1-1]==str1[len1-1] and str0[i+(len1-1)//2]==str1[(len1-1)//2]:
#         while j<len1:
#             if str0[i]==str1[j]:
#                 j+=1
#                 i+=1
#             else:
#                 j=0
#                 i=i+j
#         break
# print(i-len1)



# str0='b'
# str1='b'
# len0=len(str0)
# len1=len(str1)
# i=j=0
# for i in range(len0-len1):
#     if str0[i]!=str1[0]:#确定i的位置
#              i+=1
#     if str0[i:i+len1]==str1:
#         print(i)
#         break
#     else:
#         i+=1
# print(i)

