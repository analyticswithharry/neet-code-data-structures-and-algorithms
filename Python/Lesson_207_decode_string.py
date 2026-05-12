# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 207 -- Decode String
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 104
# =============================================================
#
# QUESTION:
#   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
# =============================================================
def decodeString(s):
    st=[]; cur=""; k=0
    for ch in s:
        if ch.isdigit(): k=k*10+int(ch)
        elif ch=='[': st.append((cur,k)); cur=""; k=0
        elif ch==']':
            pre,n=st.pop(); cur=pre+cur*n
        else: cur+=ch
    return cur

if __name__=="__main__":
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
