// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 043 -- Container With Most Water
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given heights, find two lines that with the x-axis form a container
//   holding the most water. Return the max area.
//
//   Example: [1,8,6,2,5,4,8,3,7] -> 49
// =============================================================

public class Lesson043_ContainerWithMostWater {
    public int maxArea(int[] h) {
        int i=0, j=h.length-1, best=0;
        while (i<j) {
            best = Math.max(best, (j-i)*Math.min(h[i],h[j]));
            if (h[i]<h[j]) i++; else j--;
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new Lesson043_ContainerWithMostWater().maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
    }
}
