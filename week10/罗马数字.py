# Author: Lilbox
# Time:2022/1/8 20:08

#
# strr="MCMXCIV"
# lis=[]
# dic={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# for i, ch in enumerate(s):
#     value = Solution.SYMBOL_VALUES[ch]
# result=0
# le=len(strr)
# for j in range(le):
#     for i in dic:
#         if i in strr:
#             result+=dic.get(i)
#         else:
#             lis.append(strr[j])
# for j in range(le):
#     lis.append(strr[j])
#     print(lis[j])
# for i in range(le):
#     if lis[i]=='V':
#         result=result+5
#     elif lis[i]=='I':
#         j=i+1
#         if lis[j] == 'V':
#             result+=4
#             i+=2
#         elif lis[j] =='X':
#             result+=9
#             i+=2
#         else:
#             result+=1
#     elif lis[i] == 'X':
#         j=i+1
#         if lis[j] == 'L':
#             result += 40
#             i += 2
#         elif lis[j] == 'C':
#             result += 90
#             i += 2
#         else:
#             result += 10
#     elif lis[i] == 'L':
#         result = result + 50
#     elif lis[i] == 'C':
#         j=i+1
#         if lis[j] == 'D':
#             result += 400
#             i += 2
#         elif lis[j] == 'M':
#             result += 900
#             i += 2
#         else:
#             result += 1000
#     elif lis[i] == 'D':
#         result = result + 500
#     elif lis[i] == 'M':
#         resulstre='abcd'
# for i,j in enumerate(stre):
#     print(i,j)t = result + 1000
# print(result)

class Solution:
    Symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

def romanToInt(self, s: str) -> int:
    le = len(s)
    result = 0
    for i, ch in enumerate(s):
        value = Solution.Symbol_values[ch]
        if i < le - 1 and value < Solution.Symbol_values[s[i + 1]]:
            result -= value
        else:
            result += value
    return result
