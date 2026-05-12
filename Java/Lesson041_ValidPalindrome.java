// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 041 -- Valid Palindrome
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Return true if s is a palindrome considering only alphanumeric chars
//   and ignoring case.
//
//   Example: "A man, a plan, a canal: Panama" -> true
// =============================================================

public class Lesson041_ValidPalindrome {
    public boolean isPalindrome(String s) {
        int i=0, j=s.length()-1;
        while (i<j) {
            while (i<j && !Character.isLetterOrDigit(s.charAt(i))) i++;
            while (i<j && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i++; j--;
        }
        return true;
    }
    public static void main(String[] a){
        Lesson041_ValidPalindrome s = new Lesson041_ValidPalindrome();
        System.out.println(s.isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(s.isPalindrome("race a car"));
    }
}
