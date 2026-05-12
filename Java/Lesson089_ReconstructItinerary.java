// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 089 -- Reconstruct Itinerary
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 45
// =============================================================
//
// QUESTION:
//   Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.
// =============================================================

import java.util.*;
public class Lesson089_ReconstructItinerary {
    public List<String> findItinerary(List<List<String>> tickets){
        Map<String, PriorityQueue<String>> g = new HashMap<>();
        for (List<String> t: tickets) g.computeIfAbsent(t.get(0), k->new PriorityQueue<>()).add(t.get(1));
        Deque<String> st = new ArrayDeque<>(); st.push("JFK");
        LinkedList<String> res = new LinkedList<>();
        while (!st.isEmpty()){
            while (g.containsKey(st.peek()) && !g.get(st.peek()).isEmpty()) st.push(g.get(st.peek()).poll());
            res.addFirst(st.pop());
        }
        return res;
    }
    public static void main(String[] a){
        List<List<String>> t = Arrays.asList(Arrays.asList("MUC","LHR"),Arrays.asList("JFK","MUC"),Arrays.asList("SFO","SJC"),Arrays.asList("LHR","SFO"));
        System.out.println(new Lesson089_ReconstructItinerary().findItinerary(t));
    }
}
