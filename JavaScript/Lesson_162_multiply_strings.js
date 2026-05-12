// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 162 -- Multiply Strings
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
// =============================================================
function mul(a,b){if(a==="0"||b==="0")return "0";const n=a.length,m=b.length,r=new Array(n+m).fill(0);for(let i=n-1;i>=0;i--)for(let j=m-1;j>=0;j--){const p=(a.charCodeAt(i)-48)*(b.charCodeAt(j)-48);const s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=Math.floor(s/10);}return r.join("").replace(/^0+/,"")||"0";}
console.log(mul("123","456"));
