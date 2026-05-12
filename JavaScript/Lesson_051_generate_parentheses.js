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

var generateParenthesis = function(n) {
    const res = [];
    const bt = (cur, o, c) => {
        if (cur.length === 2*n) { res.push(cur); return; }
        if (o < n) bt(cur+"(", o+1, c);
        if (c < o) bt(cur+")", o, c+1);
    };
    bt("", 0, 0);
    return res;
};
console.log(generateParenthesis(3));
