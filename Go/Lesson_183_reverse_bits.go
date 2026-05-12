//go:build ignore

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
package main
import "fmt"
func reverseBits(n uint32) uint32 { var r uint32; for i:=0;i<32;i++ { r=(r<<1)|(n&1); n>>=1 }; return r }
func main(){ fmt.Println(reverseBits(43261596)) }
