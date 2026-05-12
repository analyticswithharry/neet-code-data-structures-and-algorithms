// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 183 -- Reverse Bits
// Category   : Bit Manipulation
// Difficulty : Easy
// Study Plan : Day 92
// =============================================================
//
// QUESTION:
//   Reverse bits of a given 32-bit unsigned integer.
// =============================================================
function reverseBits(n){let r=0;for(let i=0;i<32;i++){r=(r<<1)|(n&1);n>>>=1;}return r>>>0;}
console.log(reverseBits(0b00000010100101000001111010011100));
