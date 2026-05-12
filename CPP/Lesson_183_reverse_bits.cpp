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
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <numeric>
#include <functional>
#include <cmath>
using namespace std;
uint32_t reverseBits(uint32_t n){uint32_t r=0;for(int i=0;i<32;i++){r=(r<<1)|(n&1);n>>=1;}return r;}
int main(){cout<<reverseBits(0b00000010100101000001111010011100)<<"\n";}
