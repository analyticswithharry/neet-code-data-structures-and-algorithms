// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 021 -- Baseball Game
// Category   : Stack
// Difficulty : Easy
// Study Plan : Day 11
// =============================================================
//
// QUESTION:
//   You are keeping the scores for a baseball game. Operations:
//     Integer x : record a new score x
//     '+'       : record sum of previous two scores
//     'D'       : record double of previous score
//     'C'       : invalidate the previous score, removing it
//   Return the sum of all the scores after all operations.
//
//   Example:
//     Input : ops = ["5","2","C","D","+"]
//     Output: 30   (records: 5, 10, 15)
// =============================================================

var calPoints = function(ops) {
    const st = [];
    for (const o of ops) {
        if (o === '+') st.push(st[st.length-1] + st[st.length-2]);
        else if (o === 'D') st.push(2 * st[st.length-1]);
        else if (o === 'C') st.pop();
        else st.push(parseInt(o, 10));
    }
    return st.reduce((a,b) => a+b, 0);
};
console.log(calPoints(["5","2","C","D","+"]));
