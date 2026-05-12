# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 185 -- Jump Game VII
# Category   : Greedy
# Difficulty : Medium
# Study Plan : Day 93
# =============================================================
#
# QUESTION:
#   Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?
# =============================================================
def canReach(s,mn,mx):
    n=len(s)
    if s[-1]!='0' or s[0]!='0': return False
    pre=[0]*(n+1); reach=[False]*n; reach[0]=True; pre[1]=1
    for i in range(1,n):
        if s[i]=='0':
            lo=max(0,i-mx); hi=i-mn
            if lo<=hi:
                if pre[hi+1]-pre[lo]>0: reach[i]=True
        pre[i+1]=pre[i]+(1 if reach[i] else 0)
    return reach[n-1]

if __name__=="__main__":
    print(canReach("011010",2,3))
    print(canReach("01101110",2,3))
