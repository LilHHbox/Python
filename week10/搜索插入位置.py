# Author: Lilbox
# Time:2022/1/13 10:51



#二分法


def divway(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1
    if left==right:
        if target<=nums[0]:
            print(0)
        else:
            print(1)
    else:
        while left!=right-1 :
            if target<=nums[(left+right)//2]:
                 right=(left+right)//2
            else:
                 left=(left+right)//2
        # if left == right - 1:
        if nums[left]>=target:
            if nums[left]==target:
               print(left)
            else:
                print(0)
        elif nums[right]<=target:
            if nums[right]==target:
               print(right)
            else:
                print(right+1)
        elif nums[left]<target<nums[right]:
            print(left+1)

lis=[3]
target=4


divway(lis,target)