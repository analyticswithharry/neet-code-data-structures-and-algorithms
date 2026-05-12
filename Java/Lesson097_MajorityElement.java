// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 097 -- Majority Element
// Category   : Arrays and Hashing
// Difficulty : Easy
// Study Plan : Day 49
// =============================================================
//
// QUESTION:
//   Given an array of size n, return the element that appears more than n/2 times.
// =============================================================

public class Lesson097_MajorityElement {
    public int majorityElement(int[] nums){
        int cand=0, cnt=0;
        for (int n: nums){ if (cnt==0) cand=n; cnt += n==cand?1:-1; }
        return cand;
    }
    public static void main(String[] a){
        Lesson097_MajorityElement x=new Lesson097_MajorityElement();
        System.out.println(x.majorityElement(new int[]{3,2,3}));
        System.out.println(x.majorityElement(new int[]{2,2,1,1,1,2,2}));
    }
}
