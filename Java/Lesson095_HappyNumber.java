// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 095 -- Happy Number
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 48
// =============================================================
//
// QUESTION:
//   A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.
// =============================================================

import java.util.*;
public class Lesson095_HappyNumber {
    public boolean isHappy(int n){
        Set<Integer> seen = new HashSet<>();
        while (n!=1 && !seen.contains(n)){
            seen.add(n); int s=0;
            while (n>0){ int d=n%10; s+=d*d; n/=10; } n=s;
        }
        return n==1;
    }
    public static void main(String[] a){
        Lesson095_HappyNumber x=new Lesson095_HappyNumber(); System.out.println(x.isHappy(19)); System.out.println(x.isHappy(2));
    }
}
