# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 090 -- Swim In Rising Water
# Category   : Advanced Graphs
# Difficulty : Hard
# Study Plan : Day 45
# =============================================================
#
# QUESTION:
#   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
# =============================================================

import heapq
class Solution:
    def swimInWater(self, grid):
        n = len(grid); h=[(grid[0][0],0,0)]; seen={(0,0)}; ans=0
        while h:
            v,r,c = heapq.heappop(h); ans = max(ans,v)
            if r==n-1 and c==n-1: return ans
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen:
                    seen.add((nr,nc)); heapq.heappush(h,(grid[nr][nc],nr,nc))
        return -1

if __name__ == "__main__":
    print(Solution().swimInWater([[0,2],[1,3]]))
