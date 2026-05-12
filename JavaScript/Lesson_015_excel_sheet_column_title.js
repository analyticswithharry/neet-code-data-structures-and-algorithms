// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 015 -- Excel Sheet Column Title
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   Given an integer columnNumber, return its corresponding column title
//   as it appears in an Excel sheet.
//
//   Example:
//     1  -> A
//     28 -> AB
//     701 -> ZY
// =============================================================

var convertToTitle = function(n) {
    let out = "";
    while (n > 0) { n--; out = String.fromCharCode(65 + n % 26) + out; n = Math.floor(n / 26); }
    return out;
};
console.log(convertToTitle(1), convertToTitle(28), convertToTitle(701));
