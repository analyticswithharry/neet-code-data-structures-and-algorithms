// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 208 -- Maximum Frequency Stack
// Category   : Stack
// Difficulty : Hard
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Push/pop a stack returning the most-frequent element (ties: most recent).
// =============================================================
import java.util.*;
public class Lesson208_MaximumFrequencyStack{
  static class FreqStack{Map<Integer,Integer> f=new HashMap<>();Map<Integer,Deque<Integer>> g=new HashMap<>();int maxf=0;
    void push(int v){int c=f.getOrDefault(v,0)+1;f.put(v,c);if(c>maxf)maxf=c;g.computeIfAbsent(c,k->new ArrayDeque<>()).push(v);}
    int pop(){Deque<Integer> d=g.get(maxf);int v=d.pop();f.put(v,f.get(v)-1);if(d.isEmpty())maxf--;return v;}}
  public static void main(String[]a){FreqStack fs=new FreqStack();for(int x:new int[]{5,7,5,7,4,5})fs.push(x);List<Integer> r=new ArrayList<>();for(int i=0;i<4;i++)r.add(fs.pop());System.out.println(r);}
}
