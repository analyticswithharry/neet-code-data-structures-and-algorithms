# NeetCode DSA Lessons — 6 Languages

> **250 problems. 6 languages. 1 goal: master DSA.**

**Author :** [@analyticswithharry2026](https://github.com/analyticswithharry2026)  
**YouTube :** Analytics with Harry  
**License :** MIT

---

## Languages Covered

| Language   | Folder        | Extension |
| ---------- | ------------- | --------- |
| Python     | `Python/`     | `.py`     |
| JavaScript | `JavaScript/` | `.js`     |
| Java       | `Java/`       | `.java`   |
| C++        | `CPP/`        | `.cpp`    |
| Go         | `Go/`         | `.go`     |
| R          | `R/`          | `.R`      |

---

## How to Run a Lesson

### Python

```bash
python3 Python/Lesson_001_reverse_string.py
```

### JavaScript (Node.js)

```bash
node JavaScript/Lesson_001_reverse_string.js
```

### Java

```bash
cd Java
javac Lesson001_ReverseString.java
java  Lesson001_ReverseString
```

### C++

```bash
cd CPP
g++ -std=c++17 -o lesson Lesson_001_reverse_string.cpp && ./lesson
```

### Go

```bash
cd Go
go run Lesson_001_reverse_string.go
```

### R

```bash
Rscript R/Lesson_001_reverse_string.R
```

---

## Lessons Table

| #   | Title                              | Category      | Difficulty | Day | LeetCode                                                                |
| --- | ---------------------------------- | ------------- | ---------- | --- | ----------------------------------------------------------------------- |
| 001 | Reverse String                     | Two Pointers  | Easy       | 1   | [#344](https://leetcode.com/problems/reverse-string/)                   |
| 002 | Two Sum II – Input Array Is Sorted | Two Pointers  | Medium     | 1   | [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| 003 | Reverse Linked List                | Linked List   | Easy       | 2   | [#206](https://leetcode.com/problems/reverse-linked-list/)              |
| 004 | Merge Two Sorted Lists             | Linked List   | Easy       | 2   | [#21](https://leetcode.com/problems/merge-two-sorted-lists/)            |
| 005 | Binary Tree Inorder Traversal      | Trees         | Easy       | 3   | [#94](https://leetcode.com/problems/binary-tree-inorder-traversal/)     |
| 006 | Binary Tree Preorder Traversal     | Trees         | Easy       | 3   | [#144](https://leetcode.com/problems/binary-tree-preorder-traversal/)   |
| 007 | Lemonade Change                    | Greedy        | Easy       | 4   | [#860](https://leetcode.com/problems/lemonade-change/)                  |
| 008 | Maximum Subarray                   | Greedy / DP   | Medium     | 4   | [#53](https://leetcode.com/problems/maximum-subarray/)                  |
| 009 | Binary Search                      | Binary Search | Easy       | 5   | [#704](https://leetcode.com/problems/binary-search/)                    |
| 010 | Search Insert Position             | Binary Search | Easy       | 5   | [#35](https://leetcode.com/problems/search-insert-position/)            |

> More lessons added continuously. Final goal: **250 problems**.

---

## Study Plan

Full 125-day study plan is in:  
`../extracted/neetcode-250-guide-main/NeetCode_250_Study_Plan_2026-05-12.md`

---

## Adding More Lessons

Each lesson file is generated from `generate_lessons.py`.

1. Open `generate_lessons.py`
2. Add a new entry to the `LESSONS` list following the existing pattern:

```python
{
    "num": 11, "day": 6,
    "title": "Your Problem Title",
    "category": "Category Name",
    "difficulty": "Easy | Medium | Hard",
    "lc_num": 1234, "lc_slug": "problem-slug",
    "solutions": {
        "Python":     "...solution code...",
        "JavaScript": "...solution code...",
        "Java":       "...solution code...",
        "CPP":        "...solution code...",
        "Go":         "...solution code...",
        "R":          "...solution code...",
    }
}
```

3. Run: `python3 generate_lessons.py`

---

## File Structure

```
NeetCode/
├── generate_lessons.py     ← single source of truth for all solutions
├── README.md
├── Python/
│   ├── Lesson_001_reverse_string.py
│   ├── Lesson_002_two_sum_ii_input_array_is_sorted.py
│   └── ...
├── JavaScript/
│   └── ...
├── Java/
│   ├── Lesson001_ReverseString.java
│   └── ...
├── CPP/
│   └── ...
├── Go/
│   └── ...
└── R/
    └── ...
```

---

## Each Lesson File Contains

1. **License header** — MIT + `@analyticswithharry2026`
2. **Problem statement** — copied from LeetCode description
3. **Approach explanation** — algorithm strategy in plain English
4. **Complexity analysis** — Time and Space
5. **Clean solution code** — idiomatic for each language
6. **Test / driver code** — runnable examples with expected output

---

_Happy coding! — @analyticswithharry2026_
