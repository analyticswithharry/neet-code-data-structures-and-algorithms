// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 181 -- Open The Lock
// Category   : Graphs
// Difficulty : Medium
// Study Plan : Day 91
// =============================================================
//
// QUESTION:
//   4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.
// =============================================================
import java.util.*;
public class Lesson181_OpenTheLock{
  static int openLock(String[] dead,String target){Set<String> D=new HashSet<>(Arrays.asList(dead));if(D.contains("0000"))return -1;if(target.equals("0000"))return 0;Set<String> seen=new HashSet<>();seen.add("0000");Deque<String> q=new ArrayDeque<>();q.add("0000");int d=0;while(!q.isEmpty()){d++;int sz=q.size();for(int k=0;k<sz;k++){String s=q.poll();for(int i=0;i<4;i++)for(int x:new int[]{-1,1}){char[] a=s.toCharArray();a[i]=(char)('0'+((a[i]-'0'+x+10)%10));String ns=new String(a);if(ns.equals(target))return d;if(!seen.contains(ns)&&!D.contains(ns)){seen.add(ns);q.add(ns);}}}}return -1;}
  public static void main(String[]a){System.out.println(openLock(new String[]{"0201","0101","0102","1212","2002"},"0202"));}
}
