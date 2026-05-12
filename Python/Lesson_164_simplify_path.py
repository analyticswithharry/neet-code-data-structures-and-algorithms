# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 164 -- Simplify Path
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 82
# =============================================================
#
# QUESTION:
#   Given a Unix-style absolute path, return the simplified canonical path.
# =============================================================
def simplify(p):
    st=[]
    for part in p.split('/'):
        if part=='' or part=='.': continue
        if part=='..':
            if st: st.pop()
        else: st.append(part)
    return '/'+'/'.join(st)

if __name__=="__main__":
    print(simplify("/a/./b/../../c/"))
    print(simplify("/home//foo/"))
