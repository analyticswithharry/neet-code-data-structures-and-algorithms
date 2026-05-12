# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 192 -- Word Break II
# Category   : Backtracking
# Difficulty : Hard
# Study Plan : Day 96
# =============================================================
#
# QUESTION:
#   Return all sentences obtainable by segmenting s using words from dict.
# =============================================================
def wordBreak(s,wd):
    w=set(wd); memo={}
    def dfs(i):
        if i==len(s): return [""]
        if i in memo: return memo[i]
        out=[]
        for j in range(i+1,len(s)+1):
            if s[i:j] in w:
                for t in dfs(j):
                    out.append(s[i:j]+(" "+t if t else ""))
        memo[i]=out; return out
    return dfs(0)

if __name__=="__main__":
    print(wordBreak("catsanddog",["cat","cats","and","sand","dog"]))
