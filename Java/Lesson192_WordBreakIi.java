// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 192 -- Word Break II
// Category   : Backtracking
// Difficulty : Hard
// Study Plan : Day 96
// =============================================================
//
// QUESTION:
//   Return all sentences obtainable by segmenting s using words from dict.
// =============================================================
import java.util.*;
public class Lesson192_WordBreakIi{
  static Map<Integer,List<String>> M; static String S; static Set<String> W;
  static List<String> dfs(int i){if(i==S.length()){List<String> r=new ArrayList<>();r.add("");return r;}if(M.containsKey(i))return M.get(i);List<String> out=new ArrayList<>();for(int j=i+1;j<=S.length();j++){String p=S.substring(i,j);if(W.contains(p))for(String t:dfs(j))out.add(p+(t.isEmpty()?"":" "+t));}M.put(i,out);return out;}
  static List<String> wordBreak(String s,List<String> wd){M=new HashMap<>();S=s;W=new HashSet<>(wd);return dfs(0);}
  public static void main(String[]a){System.out.println(wordBreak("catsanddog",Arrays.asList("cat","cats","and","sand","dog")));}
}
