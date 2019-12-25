'''
Problem Link(Hacker Rank): "https://www.hackerrank.com/challenges/piling-up/problem?h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=false"
'''

#CODE : >>>
for _ in range(int(input().strip())):
    N=int(input().strip())
    nList=list(map(int, input().strip().split()))
    stack=[]
    i=0
    j=len(nList)-1
    while(i<=j):
        if i==j:
            if stack and stack[len(stack)-1]>=nList[i]:
                stack.append(nList[i])
                i+=1
                j-=1
        else:
            if nList[i]==nList[j]:
                if stack and (stack[len(stack)-1] < nList[i] or stack[len(stack)-1] < nList[j]): break
                stack.append(nList[i])
                stack.append(nList[j])
                i+=1
                j-=1
            elif nList[i] < nList[j]:
                if stack and stack[len(stack)-1] < nList[j]: break
                stack.append(nList[j])
                j-=1
            elif nList[i] > nList[j]:
                if stack and stack[len(stack)-1] < nList[i]: break
                stack.append(nList[i])
                i+=1
    if len(stack)==len(nList): print("Yes")
    else: print("No")
