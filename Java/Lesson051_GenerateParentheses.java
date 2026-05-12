// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 051 -- Generate Parentheses
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 25
// =============================================================
//
// QUESTION:
//   Given n, return all valid combinations of n pairs of parentheses.
//
//   Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
// =============================================================

import java.util.*;
public class Lesson051_GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        bt(res, "", 0, 0, n);
        return res;
    }
    private void bt(List<String> r, String cur, int o, int c, int n) {
        if (cur.length()==2*n) { r.add(cur); return; }
        if (o<n) bt(r, cur+"(", o+1, c, n);
        if (c<o) bt(r, cur+")", o, c+1, n);
    }
    public static void main(String[] a){
        System.out.println(new Lesson051_GenerateParentheses().generateParenthesis(3));
    }
}
