# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 171 -- Partition to K Equal Sum Subsets
# Category   : Backtracking
# Difficulty : Medium
# Study Plan : Day 86
# =============================================================
#
# QUESTION:
#   Determine if nums can be partitioned into k subsets with equal sum.
# =============================================================
def canPartitionKSubsets(nums,k):
    s=sum(nums)
    if s%k: return False
    target=s//k; nums.sort(reverse=True)
    if nums[0]>target: return False
    buckets=[0]*k
    def bt(i):
        if i==len(nums): return True
        for j in range(k):
            if buckets[j]+nums[i]<=target:
                buckets[j]+=nums[i]
                if bt(i+1): return True
                buckets[j]-=nums[i]
            if buckets[j]==0: break
        return False
    return bt(0)

if __name__=="__main__":
    print(canPartitionKSubsets([4,3,2,3,5,2,1],4))
