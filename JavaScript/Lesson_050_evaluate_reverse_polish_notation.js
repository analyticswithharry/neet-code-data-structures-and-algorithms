// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 050 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 25
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation.
//
//   Example: ["2","1","+","3","*"] -> 9
// =============================================================

var evalRPN = function(tokens) {
    const st = [];
    for (const t of tokens) {
        if ("+-*/".includes(t)) {
            const b = st.pop(), a = st.pop();
            if (t==="+") st.push(a+b);
            else if (t==="-") st.push(a-b);
            else if (t==="*") st.push(a*b);
            else st.push(Math.trunc(a/b));
        } else st.push(parseInt(t));
    }
    return st[0];
};
console.log(evalRPN(["2","1","+","3","*"]));
