# Author: Lilbox
# Time:2022/1/11 9:21



#官方 本质上也是双指针
nums=[0,1,1,1,2,2,2,4,5,5]
if not nums:
    print(0)

n = len(nums)
fast = slow = 1
while fast < n:
    if nums[fast] != nums[fast - 1]:
        nums[slow] = nums[fast]
        slow += 1
    fast += 1
print(slow)

















