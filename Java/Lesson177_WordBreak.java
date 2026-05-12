// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 177 -- Word Break
// Category   : 1-D Dynamic Programming
// Difficulty : Medium
// Study Plan : Day 89
// =============================================================
//
// QUESTION:
//   Determine if string s can be segmented into words from the given dictionary.
// =============================================================
import java.util.*;
public class Lesson177_WordBreak{
  static boolean wordBreak(String s,List<String> wd){Set<String> w=new HashSet<>(wd);int n=s.length();boolean[] dp=new boolean[n+1];dp[0]=true;for(int i=1;i<=n;i++)for(int j=0;j<i;j++)if(dp[j]&&w.contains(s.substring(j,i))){dp[i]=true;break;}return dp[n];}
  public static void main(String[]a){System.out.println(wordBreak("leetcode",Arrays.asList("leet","code")));System.out.println(wordBreak("catsandog",Arrays.asList("cats","dog","sand","and","cat")));}
}
