#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        i=n-1
        j=1
        sum=1
        while i>=(n/2):
            sum+=(math.factorial(i))//((math.factorial(j))*math.factorial((i-j)))
            i-=1
            j+=1
        return sum

# @lc code=end

