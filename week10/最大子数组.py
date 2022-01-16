# Author: Lilbox
# Time:2022/1/14 8:08



num = [-2,-3,-1]
#法1：贪心算法
def maxSubArray(nums: list[int]):
    length=len(nums)
    for i in range(0,length):
        if nums[i-1]>0:
            nums[i]+=nums[i-1]
    print(max(nums))

    # max=nums[0]
    # sum=0
    # length=len(nums)
    # if length==1:
    #     print(max)
    # else:
    #     for i in range(0,length):
    #         sum+=nums[i]
    #         if sum>max:
    #             max=sum
    #         if sum<0:
    #              sum=0
    #         # elif sum<0:
    #         #     sum=0
    #     print(max)
maxSubArray(num)


