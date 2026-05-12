// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 096 -- Rotate Image
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   Rotate an n x n 2D matrix 90 degrees clockwise in-place.
// =============================================================

import java.util.*;
public class Lesson096_RotateImage {
    public void rotate(int[][] m){
        int n=m.length;
        for (int i=0;i<n;i++) for (int j=i+1;j<n;j++){ int t=m[i][j]; m[i][j]=m[j][i]; m[j][i]=t; }
        for (int[] r: m) for (int i=0,j=n-1;i<j;i++,j--){ int t=r[i]; r[i]=r[j]; r[j]=t; }
    }
    public static void main(String[] a){
        int[][] m={{1,2,3},{4,5,6},{7,8,9}}; new Lesson096_RotateImage().rotate(m);
        System.out.println(Arrays.deepToString(m));
    }
}
