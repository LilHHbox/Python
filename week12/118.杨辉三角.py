#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lis=[]
        if numRows==1:
            lis.append([1])
            return lis
        elif numRows==2:
            lis[0:]=[[1],[1,1]]  
            return lis
        lis[0:]=[[1],[1,1]]    
        lis1=list(lis[1])
        Lis=[]
        j=0
        for i in range(2,numRows):
            while j<len(lis1)-1:
                Lis.append(lis1[j]+lis1[j+1])
                j+=1
            Lis.insert(0, 1)
            Lis.append(1)
            lis.append(Lis)
            j=0
            i+=1
            lis1 = Lis
            Lis=[]
        return lis

# @lc code=end

