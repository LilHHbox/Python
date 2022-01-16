# Author: Lilbox
# Time:2022/1/10 9:49


s='()'
num=len(s)
lis=[0]
numlist=0
for i in range(num):
    if s[i]=='{' or s[i]=='[' or s[i]=='(':
        lis.append(s[i])#开放符号入栈
        numlist = len(lis) - 1#指向栈顶的指针

    elif s[i]=='}':
        if lis[numlist]!='{' or lis[numlist]==0:#符号不匹配或者栈为空
            print(False)
            break
        # else:
        #     lis.pop()
        #     numlist-=1

    elif s[i] == ']':
        if lis[numlist] != '[' or lis[numlist] == 0:  # 符号不匹配或者栈为空
            print(False)
            break
        # else:
        #     lis.pop()
        #     numlist -= 1

    elif s[i] == ')':
        if lis[numlist] != '(' or lis[numlist] == 0:  # 符号不匹配或者栈为空
            print(False)
            break
    else:
        lis.pop()
        numlist -= 1

if lis[numlist]==0:#栈为空的时候
    print(True)
else:
    print(False)









