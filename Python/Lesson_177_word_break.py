# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 177 -- Word Break
# Category   : 1-D Dynamic Programming
# Difficulty : Medium
# Study Plan : Day 89
# =============================================================
#
# QUESTION:
#   Determine if string s can be segmented into words from the given dictionary.
# =============================================================
def wordBreak(s,wd):
    w=set(wd); n=len(s); dp=[False]*(n+1); dp[0]=True
    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in w:
                dp[i]=True; break
    return dp[n]

if __name__=="__main__":
    print(wordBreak("leetcode",["leet","code"]))
    print(wordBreak("applepenapple",["apple","pen"]))
    print(wordBreak("catsandog",["cats","dog","sand","and","cat"]))
