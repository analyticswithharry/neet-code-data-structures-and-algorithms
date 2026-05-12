// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 022 -- Valid Parentheses
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   Given a string s containing just the characters '(', ')', '{', '}',
//   '[' and ']', determine if the input string is valid. An input string is
//   valid if open brackets are closed by the same type of brackets in the
//   correct order.
//
//   Example:
//     Input : "()[]{}"   Output: true
//     Input : "(]"       Output: false
// =============================================================

var isValid = function(s) {
    const m = {')':'(', ']':'[', '}':'{'};
    const st = [];
    for (const c of s) {
        if (m[c]) { if (st.pop() !== m[c]) return false; }
        else st.push(c);
    }
    return st.length === 0;
};
console.log(isValid("()[]{}"), isValid("(]"));
