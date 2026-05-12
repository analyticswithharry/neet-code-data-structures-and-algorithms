// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 017 -- Climbing Stairs
// Category   : 1-D Dynamic Programming
// Difficulty : Easy
// Study Plan : Day 9
// =============================================================
//
// QUESTION:
//   You are climbing a staircase. It takes n steps to reach the top. Each
//   time you can climb 1 or 2 steps. In how many distinct ways can you climb
//   to the top?
//
//   Example:
//     Input : n = 2  -> 2
//     Input : n = 3  -> 3
// =============================================================

public class Lesson017_ClimbingStairs {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 0; i < n; i++) { int t = a + b; a = b; b = t; }
        return a;
    }
    public static void main(String[] args) {
        Lesson017_ClimbingStairs s = new Lesson017_ClimbingStairs();
        System.out.println(s.climbStairs(2) + " " + s.climbStairs(3) + " " + s.climbStairs(5));
    }
}
