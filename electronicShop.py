'''
Electronics Shop:>>> (Hacker Rank)>>>
'''

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    if not drives and not keyboards: return -1
    if not drives or not keyboards: return -1
    drives.sort()
    keyboards.sort()
    seperateList = []
    for i in range(len(keyboards)-1, -1, -1):
        currentMax = keyboards[i]
        if currentMax < b:
            inner = len(drives)-1
            while inner >= 0:
                if drives[inner] + currentMax <= b:
                    seperateList.append(drives[inner] + currentMax)
                    break
                inner -= 1
    if seperateList: return max(seperateList)
    else: return -1
