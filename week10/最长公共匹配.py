# Author: Lilbox
# Time:2022/1/8 21:20


# dic={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# # for i in dic:
# #     print(dic.get(i))
# s='acd'
# s1=s.replace('ac','')
# print(len(s1))

s4=['ccc','cc','ccc']
le=len(s4)
str0=str(s4[0])
le1=len(str0)
arry=[]

for i in range(1,le):
    count=0
    for j,ch in enumerate(s4[i]):
        if le1-1>=j:
            if str0[j]==ch:
                count+=1

        else:
            break
    arry.append(count)
smallest=arry[0]
for i in range(1,len(arry)):
    if arry[i]<smallest:
        smallest=arry[i]
print(str0[0:smallest])



#官方：
#法一
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:#判断空
            return ""

        prefix, count = strs[0], len(strs)#把第一个字符串赋给prefix 把数组长度赋给count
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])#调用lcp函数
            if not prefix:#判断空
                break
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0  #首先先找出比较对象长度最小的，并赋给length
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#法二
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):#情况1是i和某一个字符串长度已经相等了 情况2是某个字符不等了
                return strs[0][:i]

        return strs[0]

