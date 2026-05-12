// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 056 -- Koko Eating Bananas
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 28
// =============================================================
//
// QUESTION:
//   Koko eats bananas at speed k per hour. Given piles and h hours,
//   return the minimum k such that she finishes within h hours.
//
//   Example: piles=[3,6,7,11], h=8 -> 4
// =============================================================

public class Lesson056_KokoEatingBananas {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 0;
        for (int p: piles) r = Math.max(r, p);
        while (l < r) {
            int mid = l + (r-l)/2;
            long hrs = 0;
            for (int p: piles) hrs += (p + mid - 1) / mid;
            if (hrs <= h) r = mid; else l = mid+1;
        }
        return l;
    }
    public static void main(String[] a){
        System.out.println(new Lesson056_KokoEatingBananas().minEatingSpeed(new int[]{3,6,7,11}, 8));
    }
}
