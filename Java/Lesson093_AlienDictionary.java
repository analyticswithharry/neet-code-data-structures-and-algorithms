// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 093 -- Alien Dictionary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.
// =============================================================

import java.util.*;
public class Lesson093_AlienDictionary {
    public String alienOrder(String[] words){
        Map<Character, Set<Character>> g = new HashMap<>();
        Map<Character, Integer> ind = new HashMap<>();
        for (String w: words) for (char c: w.toCharArray()){ g.putIfAbsent(c,new HashSet<>()); ind.putIfAbsent(c,0); }
        for (int i=0;i<words.length-1;i++){
            String a=words[i], b=words[i+1]; boolean found=false;
            int m=Math.min(a.length(),b.length());
            for (int j=0;j<m;j++){
                char x=a.charAt(j), y=b.charAt(j);
                if (x!=y){ if (g.get(x).add(y)) ind.merge(y,1,Integer::sum); found=true; break; }
            }
            if (!found && a.length()>b.length()) return "";
        }
        Deque<Character> q = new ArrayDeque<>();
        for (var e: ind.entrySet()) if (e.getValue()==0) q.add(e.getKey());
        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()){
            char c=q.poll(); sb.append(c);
            for (char nx: g.get(c)){ ind.merge(nx,-1,Integer::sum); if (ind.get(nx)==0) q.add(nx); }
        }
        return sb.length()==ind.size() ? sb.toString() : "";
    }
    public static void main(String[] a){
        System.out.println(new Lesson093_AlienDictionary().alienOrder(new String[]{"wrt","wrf","er","ett","rftt"}));
    }
}
