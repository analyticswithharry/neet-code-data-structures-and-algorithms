// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 041 -- Valid Palindrome
// Category   : Two Pointers
// Difficulty : Easy
// Study Plan : Day 20
// =============================================================
//
// QUESTION:
//   Return true if s is a palindrome considering only alphanumeric chars
//   and ignoring case.
//
//   Example: "A man, a plan, a canal: Panama" -> true
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
class Solution {
public:
    bool isPalindrome(string s) {
        int i=0, j=s.size()-1;
        while (i<j) {
            while (i<j && !isalnum((unsigned char)s[i])) i++;
            while (i<j && !isalnum((unsigned char)s[j])) j--;
            if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])) return false;
            i++; j--;
        }
        return true;
    }
};
int main(){ Solution s; cout<<s.isPalindrome("A man, a plan, a canal: Panama")<<" "<<s.isPalindrome("race a car")<<endl; }
