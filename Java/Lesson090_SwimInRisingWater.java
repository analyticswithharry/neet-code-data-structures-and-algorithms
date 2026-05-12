// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 090 -- Swim In Rising Water
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.
// =============================================================

import java.util.*;
public class Lesson090_SwimInRisingWater {
    public int swimInWater(int[][] grid){
        int n=grid.length; PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        pq.add(new int[]{grid[0][0],0,0}); boolean[][] seen=new boolean[n][n]; seen[0][0]=true; int ans=0;
        int[][] d={{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()){
            int[] x=pq.poll(); ans=Math.max(ans,x[0]);
            if (x[1]==n-1 && x[2]==n-1) return ans;
            for (int[] dd: d){ int nr=x[1]+dd[0], nc=x[2]+dd[1];
                if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]){ seen[nr][nc]=true; pq.add(new int[]{grid[nr][nc],nr,nc}); } }
        } return -1;
    }
    public static void main(String[] a){
        System.out.println(new Lesson090_SwimInRisingWater().swimInWater(new int[][]{{0,2},{1,3}}));
    }
}
