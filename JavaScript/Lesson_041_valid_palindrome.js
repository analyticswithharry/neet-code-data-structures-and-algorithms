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

var isPalindrome = function(s) {
    const isAN = c => /[a-z0-9]/i.test(c);
    let i=0, j=s.length-1;
    while (i<j) {
        while (i<j && !isAN(s[i])) i++;
        while (i<j && !isAN(s[j])) j--;
        if (s[i].toLowerCase()!==s[j].toLowerCase()) return false;
        i++; j--;
    }
    return true;
};
console.log(isPalindrome("A man, a plan, a canal: Panama"), isPalindrome("race a car"));
