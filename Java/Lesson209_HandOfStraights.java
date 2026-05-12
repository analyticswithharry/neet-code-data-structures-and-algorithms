// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 209 -- Hand of Straights
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 105
// =============================================================
//
// QUESTION:
//   Can hand be rearranged into groups of size W of consecutive cards?
// =============================================================
import java.util.*;
public class Lesson209_HandOfStraights{
  static boolean isNStraightHand(int[] h,int W){if(h.length%W!=0)return false;TreeMap<Integer,Integer> c=new TreeMap<>();for(int x:h)c.merge(x,1,Integer::sum);for(int x:new ArrayList<>(c.keySet())){int cnt=c.getOrDefault(x,0);if(cnt>0){for(int k=0;k<W;k++){int v=c.getOrDefault(x+k,0);if(v<cnt)return false;if(v==cnt)c.remove(x+k);else c.put(x+k,v-cnt);}}}return true;}
  public static void main(String[]a){System.out.println(isNStraightHand(new int[]{1,2,3,6,2,3,4,7,8},3));System.out.println(isNStraightHand(new int[]{1,2,3,4,5},4));}
}
