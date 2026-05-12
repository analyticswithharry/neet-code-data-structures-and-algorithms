// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 055 -- Search a 2D Matrix
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 27
// =============================================================
//
// QUESTION:
//   Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
//   search for target.
//
//   Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true
// =============================================================

public class Lesson055_SearchA2dMatrix {
    public boolean searchMatrix(int[][] m, int target) {
        if (m.length==0 || m[0].length==0) return false;
        int rows = m.length, cols = m[0].length;
        int l = 0, r = rows*cols - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            int v = m[mid/cols][mid%cols];
            if (v == target) return true;
            if (v < target) l = mid+1; else r = mid-1;
        }
        return false;
    }
    public static void main(String[] a){
        int[][] m = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        Lesson055_SearchA2dMatrix s = new Lesson055_SearchA2dMatrix();
        System.out.println(s.searchMatrix(m, 3));
        System.out.println(s.searchMatrix(m, 13));
    }
}
