// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 108 -- Evaluate Reverse Polish Notation
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 54
// =============================================================
//
// QUESTION:
//   Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.
// =============================================================

var evalRPN = function(tokens){
  const st=[];
  for (const t of tokens){
    if ("+-*/".includes(t) && t.length===1){
      const b=st.pop(), a=st.pop();
      if (t==='+') st.push(a+b);
      else if (t==='-') st.push(a-b);
      else if (t==='*') st.push(a*b);
      else st.push(a/b<0 ? Math.ceil(a/b) : Math.floor(a/b));
    } else st.push(parseInt(t,10));
  }
  return st[0];
};
console.log(evalRPN(["2","1","+","3","*"]), evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]));
