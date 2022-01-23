# Author: Lilbox
# Time:2022/1/17 9:21



x=10

left=0
right=x

# if x==0 or x==1:
#     print(x)
# while left!=right-1:
#     el=(left+right)//2
#     if (el-1)*(el-1)>=x:
#         right=el
#     elif el*el<=x:
#         left=el
#     elif el*el>x and (el-1)*(el-1)<x:
#         print(el-1)
#         break
# print(left)
#
# #官方
# # class Solution:
# #     def mySqrt(self, x: int) -> int:
l, r, ans = 0, x, -1
while l <= r:
    mid = (l + r) // 2
    if mid * mid <= x:
        ans = mid
        l = mid + 1
    else:

        r = mid - 1
print(ans)

