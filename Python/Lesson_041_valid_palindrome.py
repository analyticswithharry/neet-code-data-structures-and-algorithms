# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 041 -- Valid Palindrome
# Category   : Two Pointers
# Difficulty : Easy
# Study Plan : Day 20
# =============================================================
#
# QUESTION:
#   Return true if s is a palindrome considering only alphanumeric chars
#   and ignoring case.
#
#   Example: "A man, a plan, a canal: Panama" -> true
# =============================================================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while i<j and not s[i].isalnum(): i+=1
            while i<j and not s[j].isalnum(): j-=1
            if s[i].lower() != s[j].lower(): return False
            i+=1; j-=1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
