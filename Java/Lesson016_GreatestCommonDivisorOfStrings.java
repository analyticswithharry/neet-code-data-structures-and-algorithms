// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 016 -- Greatest Common Divisor of Strings
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   For two strings s and t, we say "t divides s" if s = t + t + ... + t.
//   Return the largest string x such that x divides both str1 and str2.
//
//   Example:
//     Input : str1="ABCABC", str2="ABC"     Output: "ABC"
//     Input : str1="ABABAB", str2="ABAB"    Output: "AB"
//     Input : str1="LEET",   str2="CODE"    Output: ""
// =============================================================

public class Lesson016_GreatestCommonDivisorOfStrings {
    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    public String gcdOfStrings(String s1, String s2) {
        if (!(s1+s2).equals(s2+s1)) return "";
        return s1.substring(0, gcd(s1.length(), s2.length()));
    }
    public static void main(String[] args) {
        Lesson016_GreatestCommonDivisorOfStrings s = new Lesson016_GreatestCommonDivisorOfStrings();
        System.out.println(s.gcdOfStrings("ABCABC","ABC") + "|" + s.gcdOfStrings("ABABAB","ABAB") + "|" + s.gcdOfStrings("LEET","CODE"));
    }
}
