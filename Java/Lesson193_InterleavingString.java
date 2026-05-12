// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 193 -- Interleaving String
// Category   : 2-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 97
// =============================================================
//
// QUESTION:
//   Determine whether s3 can be formed by interleaving s1 and s2.
// =============================================================
public class Lesson193_InterleavingString{
  static boolean isInterleave(String a,String b,String c){if(a.length()+b.length()!=c.length())return false;boolean[][] dp=new boolean[a.length()+1][b.length()+1];dp[0][0]=true;for(int i=0;i<=a.length();i++)for(int j=0;j<=b.length();j++){if(i>0 && a.charAt(i-1)==c.charAt(i+j-1)) dp[i][j]|=dp[i-1][j];if(j>0 && b.charAt(j-1)==c.charAt(i+j-1)) dp[i][j]|=dp[i][j-1];}return dp[a.length()][b.length()];}
  public static void main(String[]a){System.out.println(isInterleave("aabcc","dbbca","aadbbcbcac"));System.out.println(isInterleave("aabcc","dbbca","aadbbbaccc"));}
}
