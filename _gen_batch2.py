"""Batch 2: lessons 011-035 with full question + working solution per file."""
from _lesson_writer import write_lessons

LESSONS = []

# 011 - Implement Trie Prefix Tree
LESSONS.append((11, "Implement Trie Prefix Tree", "Tries", "Medium", 6,
"""Implement the Trie class with:
  insert(word)        - inserts the word
  search(word)        - returns true if word is in trie
  startsWith(prefix)  - returns true if any word starts with prefix

Example:
  trie = Trie()
  trie.insert("apple")
  trie.search("apple")   -> True
  trie.search("app")     -> False
  trie.startsWith("app") -> True
  trie.insert("app")
  trie.search("app")     -> True""",
{
"Python":'''
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    def insert(self, w):
        n = self
        for c in w:
            n = n.children.setdefault(c, Trie())
        n.end = True
    def _walk(self, w):
        n = self
        for c in w:
            if c not in n.children: return None
            n = n.children[c]
        return n
    def search(self, w): n = self._walk(w); return bool(n) and n.end
    def startsWith(self, p): return self._walk(p) is not None

if __name__ == "__main__":
    t = Trie(); t.insert("apple")
    print(t.search("apple"), t.search("app"), t.startsWith("app"))
    t.insert("app"); print(t.search("app"))
''',
"JavaScript":'''
class Trie {
    constructor() { this.ch = {}; this.end = false; }
    insert(w) { let n = this; for (const c of w) { if (!n.ch[c]) n.ch[c] = new Trie(); n = n.ch[c]; } n.end = true; }
    _walk(w) { let n = this; for (const c of w) { if (!n.ch[c]) return null; n = n.ch[c]; } return n; }
    search(w) { const n = this._walk(w); return !!n && n.end; }
    startsWith(p) { return this._walk(p) !== null; }
}

const t = new Trie(); t.insert("apple");
console.log(t.search("apple"), t.search("app"), t.startsWith("app"));
t.insert("app"); console.log(t.search("app"));
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class Trie {
        Map<Character, Trie> ch = new HashMap<>();
        boolean end;
        public void insert(String w) {
            Trie n = this;
            for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new Trie());
            n.end = true;
        }
        Trie walk(String w) {
            Trie n = this;
            for (char c : w.toCharArray()) { n = n.ch.get(c); if (n == null) return null; }
            return n;
        }
        public boolean search(String w) { Trie n = walk(w); return n != null && n.end; }
        public boolean startsWith(String p) { return walk(p) != null; }
    }
    public static void main(String[] args) {
        Trie t = new Trie(); t.insert("apple");
        System.out.println(t.search("apple") + " " + t.search("app") + " " + t.startsWith("app"));
        t.insert("app"); System.out.println(t.search("app"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class Trie {
public:
    unordered_map<char, Trie*> ch; bool end = false;
    void insert(const string& w) {
        Trie* n = this;
        for (char c : w) { if (!n->ch.count(c)) n->ch[c] = new Trie(); n = n->ch[c]; }
        n->end = true;
    }
    Trie* walk(const string& w) {
        Trie* n = this;
        for (char c : w) { if (!n->ch.count(c)) return nullptr; n = n->ch[c]; }
        return n;
    }
    bool search(const string& w) { auto* n = walk(w); return n && n->end; }
    bool startsWith(const string& p) { return walk(p) != nullptr; }
};

int main() {
    Trie t; t.insert("apple");
    cout << boolalpha << t.search("apple") << " " << t.search("app") << " " << t.startsWith("app") << endl;
    t.insert("app"); cout << t.search("app") << endl;
}
''',
"Go":'''
package main

import "fmt"

type Trie struct { ch map[rune]*Trie; end bool }
func NewTrie() *Trie { return &Trie{ch: map[rune]*Trie{}} }
func (t *Trie) Insert(w string) {
    n := t
    for _, c := range w {
        if _, ok := n.ch[c]; !ok { n.ch[c] = NewTrie() }
        n = n.ch[c]
    }
    n.end = true
}
func (t *Trie) walk(w string) *Trie {
    n := t
    for _, c := range w {
        nx, ok := n.ch[c]; if !ok { return nil }; n = nx
    }
    return n
}
func (t *Trie) Search(w string) bool { n := t.walk(w); return n != nil && n.end }
func (t *Trie) StartsWith(p string) bool { return t.walk(p) != nil }

func main() {
    t := NewTrie(); t.Insert("apple")
    fmt.Println(t.Search("apple"), t.Search("app"), t.StartsWith("app"))
    t.Insert("app"); fmt.Println(t.Search("app"))
}
''',
"R":'''
# Trie implemented as nested environments.
new_trie <- function() { e <- new.env(hash=TRUE); e$end <- FALSE; e$ch <- new.env(hash=TRUE); e }
insert <- function(t, w) {
    n <- t
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) assign(c, new_trie(), envir=n$ch)
        n <- get(c, envir=n$ch)
    }
    n$end <- TRUE
}
walk <- function(t, w) {
    n <- t
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) return(NULL)
        n <- get(c, envir=n$ch)
    }
    n
}
search_w <- function(t, w) { n <- walk(t, w); !is.null(n) && n$end }
startsWith_t <- function(t, p) { !is.null(walk(t, p)) }

t <- new_trie(); insert(t, "apple")
print(c(search_w(t,"apple"), search_w(t,"app"), startsWith_t(t,"app")))
insert(t, "app"); print(search_w(t,"app"))
''',
}))

# 012 - Design Add And Search Words Data Structure
LESSONS.append((12, "Design Add And Search Words Data Structure", "Tries", "Medium", 6,
"""Design a data structure that supports:
  addWord(word)
  search(word)  - word may contain '.' which matches any single letter

Example:
  d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
  d.search("pad") -> False
  d.search("bad") -> True
  d.search(".ad") -> True
  d.search("b..") -> True""",
{
"Python":'''
class WordDictionary:
    def __init__(self):
        self.ch = {}
        self.end = False
    def addWord(self, w):
        n = self
        for c in w: n = n.ch.setdefault(c, WordDictionary())
        n.end = True
    def search(self, w):
        def dfs(i, n):
            if i == len(w): return n.end
            c = w[i]
            if c == '.':
                return any(dfs(i+1, x) for x in n.ch.values())
            return c in n.ch and dfs(i+1, n.ch[c])
        return dfs(0, self)

if __name__ == "__main__":
    d = WordDictionary()
    for w in ["bad","dad","mad"]: d.addWord(w)
    print(d.search("pad"), d.search("bad"), d.search(".ad"), d.search("b.."))
''',
"JavaScript":'''
class WordDictionary {
    constructor() { this.ch = {}; this.end = false; }
    addWord(w) { let n = this; for (const c of w) { if (!n.ch[c]) n.ch[c] = new WordDictionary(); n = n.ch[c]; } n.end = true; }
    search(w) {
        const dfs = (i, n) => {
            if (i === w.length) return n.end;
            const c = w[i];
            if (c === '.') return Object.values(n.ch).some(x => dfs(i+1, x));
            return n.ch[c] !== undefined && dfs(i+1, n.ch[c]);
        };
        return dfs(0, this);
    }
}
const d = new WordDictionary();
["bad","dad","mad"].forEach(w => d.addWord(w));
console.log(d.search("pad"), d.search("bad"), d.search(".ad"), d.search("b.."));
''',
"Java":'''
import java.util.*;

public class __CLASS__ {
    static class WordDictionary {
        Map<Character, WordDictionary> ch = new HashMap<>(); boolean end;
        public void addWord(String w) {
            WordDictionary n = this;
            for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new WordDictionary());
            n.end = true;
        }
        public boolean search(String w) { return dfs(0, w, this); }
        boolean dfs(int i, String w, WordDictionary n) {
            if (i == w.length()) return n.end;
            char c = w.charAt(i);
            if (c == '.') {
                for (WordDictionary x : n.ch.values()) if (dfs(i+1, w, x)) return true;
                return false;
            }
            WordDictionary nx = n.ch.get(c);
            return nx != null && dfs(i+1, w, nx);
        }
    }
    public static void main(String[] args) {
        WordDictionary d = new WordDictionary();
        for (String w : new String[]{"bad","dad","mad"}) d.addWord(w);
        System.out.println(d.search("pad") + " " + d.search("bad") + " " + d.search(".ad") + " " + d.search("b.."));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;

class WordDictionary {
public:
    unordered_map<char, WordDictionary*> ch; bool end = false;
    void addWord(const string& w) {
        WordDictionary* n = this;
        for (char c : w) { if (!n->ch.count(c)) n->ch[c] = new WordDictionary(); n = n->ch[c]; }
        n->end = true;
    }
    bool search(const string& w) { return dfs(0, w, this); }
    bool dfs(int i, const string& w, WordDictionary* n) {
        if (i == (int)w.size()) return n->end;
        char c = w[i];
        if (c == '.') {
            for (auto& [_, x] : n->ch) if (dfs(i+1, w, x)) return true;
            return false;
        }
        return n->ch.count(c) && dfs(i+1, w, n->ch[c]);
    }
};

int main() {
    WordDictionary d;
    for (auto w : {"bad","dad","mad"}) d.addWord(w);
    cout << boolalpha << d.search("pad") << " " << d.search("bad")
         << " " << d.search(".ad") << " " << d.search("b..") << endl;
}
''',
"Go":'''
package main

import "fmt"

type WordDictionary struct { ch map[byte]*WordDictionary; end bool }
func NewWD() *WordDictionary { return &WordDictionary{ch: map[byte]*WordDictionary{}} }
func (d *WordDictionary) AddWord(w string) {
    n := d
    for i := 0; i < len(w); i++ {
        c := w[i]
        if _, ok := n.ch[c]; !ok { n.ch[c] = NewWD() }
        n = n.ch[c]
    }
    n.end = true
}
func (d *WordDictionary) Search(w string) bool { return dfs(0, w, d) }
func dfs(i int, w string, n *WordDictionary) bool {
    if i == len(w) { return n.end }
    c := w[i]
    if c == '.' {
        for _, x := range n.ch { if dfs(i+1, w, x) { return true } }
        return false
    }
    nx, ok := n.ch[c]
    return ok && dfs(i+1, w, nx)
}

func main() {
    d := NewWD()
    for _, w := range []string{"bad","dad","mad"} { d.AddWord(w) }
    fmt.Println(d.Search("pad"), d.Search("bad"), d.Search(".ad"), d.Search("b.."))
}
''',
"R":'''
new_wd <- function() { e <- new.env(hash=TRUE); e$end <- FALSE; e$ch <- new.env(hash=TRUE); e }
addWord <- function(d, w) {
    n <- d
    for (c in strsplit(w, "")[[1]]) {
        if (!exists(c, envir=n$ch, inherits=FALSE)) assign(c, new_wd(), envir=n$ch)
        n <- get(c, envir=n$ch)
    }
    n$end <- TRUE
}
search_wd <- function(d, w) {
    chars <- strsplit(w, "")[[1]]
    dfs <- function(i, n) {
        if (i > length(chars)) return(n$end)
        c <- chars[i]
        if (c == ".") {
            for (k in ls(n$ch)) if (dfs(i+1, get(k, envir=n$ch))) return(TRUE)
            return(FALSE)
        }
        if (!exists(c, envir=n$ch, inherits=FALSE)) return(FALSE)
        dfs(i+1, get(c, envir=n$ch))
    }
    dfs(1, d)
}

d <- new_wd(); for (w in c("bad","dad","mad")) addWord(d, w)
print(c(search_wd(d,"pad"), search_wd(d,"bad"), search_wd(d,".ad"), search_wd(d,"b..")))
''',
}))

# 013 - Binary Tree Postorder Traversal
LESSONS.append((13, "Binary Tree Postorder Traversal", "Trees", "Easy", 7,
"""Given the root of a binary tree, return the postorder
(Left, Right, Root) traversal of its nodes' values.

Example:
  Input : root = [1,null,2,3]
  Output: [3, 2, 1]""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def postorderTraversal(self, root):
        out, st = [], []
        cur, last = root, None
        while cur or st:
            while cur: st.append(cur); cur = cur.left
            peek = st[-1]
            if peek.right and last is not peek.right:
                cur = peek.right
            else:
                out.append(peek.val); last = st.pop()
        return out

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().postorderTraversal(root))  # [3,2,1]
''',
"JavaScript":'''
function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var postorderTraversal = function(root) {
    const out = [], st = [];
    let cur = root, last = null;
    while (cur || st.length) {
        while (cur) { st.push(cur); cur = cur.left; }
        const peek = st[st.length-1];
        if (peek.right && last !== peek.right) cur = peek.right;
        else { out.push(peek.val); last = st.pop(); }
    }
    return out;
};
console.log(postorderTraversal(new TreeNode(1,null,new TreeNode(2,new TreeNode(3)))));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>(); Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root, last = null;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            TreeNode peek = st.peek();
            if (peek.right != null && last != peek.right) cur = peek.right;
            else { out.add(peek.val); last = st.pop(); }
        }
        return out;
    }
    public static void main(String[] args) {
        TreeNode r = new TreeNode(1); r.right = new TreeNode(2); r.right.left = new TreeNode(3);
        System.out.println(new __CLASS__().postorderTraversal(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(0),right(0){} };
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> out; stack<TreeNode*> st;
        TreeNode *cur = root, *last = nullptr;
        while (cur || !st.empty()) {
            while (cur) { st.push(cur); cur = cur->left; }
            TreeNode* peek = st.top();
            if (peek->right && last != peek->right) cur = peek->right;
            else { out.push_back(peek->val); last = peek; st.pop(); }
        }
        return out;
    }
};
int main() {
    auto* r = new TreeNode(1); r->right = new TreeNode(2); r->right->left = new TreeNode(3);
    for (int v : Solution().postorderTraversal(r)) cout << v << " ";
    cout << endl;
}
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func postorderTraversal(root *TreeNode) []int {
    out := []int{}; st := []*TreeNode{}
    var cur, last *TreeNode = root, nil
    for cur != nil || len(st) > 0 {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        peek := st[len(st)-1]
        if peek.Right != nil && last != peek.Right { cur = peek.Right
        } else { out = append(out, peek.Val); last = peek; st = st[:len(st)-1] }
    }
    return out
}
func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(postorderTraversal(r))
}
''',
"R":'''
postorderTraversal <- function(node) {
    if (is.null(node)) return(integer(0))
    c(postorderTraversal(node$left), postorderTraversal(node$right), node$val)
}
root <- list(val=1, left=NULL, right=list(val=2, left=list(val=3, left=NULL, right=NULL), right=NULL))
print(postorderTraversal(root))  # 3 2 1
''',
}))

# 014 - LCA of BST
LESSONS.append((14, "Lowest Common Ancestor of a Binary Search Tree", "Trees", "Medium", 7,
"""Given a binary search tree (BST), find the lowest common ancestor (LCA)
of two given nodes p and q. Both p and q exist in the BST.

Example:
  Input : root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8
  Output: 6""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val: cur = cur.left
            elif p.val > cur.val and q.val > cur.val: cur = cur.right
            else: return cur

if __name__ == "__main__":
    n0,n3,n4,n5,n7,n9 = TreeNode(0),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(7),TreeNode(9)
    n4.left,n4.right = n3,n5
    n2 = TreeNode(2,n0,n4); n8 = TreeNode(8,n7,n9)
    root = TreeNode(6,n2,n8)
    print(Solution().lowestCommonAncestor(root, n2, n8).val)  # 6
''',
"JavaScript":'''
function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var lowestCommonAncestor = function(root, p, q) {
    let cur = root;
    while (cur) {
        if (p.val < cur.val && q.val < cur.val) cur = cur.left;
        else if (p.val > cur.val && q.val > cur.val) cur = cur.right;
        else return cur;
    }
};
const n2 = new TreeNode(2), n8 = new TreeNode(8);
const root = new TreeNode(6, n2, n8);
console.log(lowestCommonAncestor(root, n2, n8).val); // 6
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode cur = root;
        while (cur != null) {
            if (p.val < cur.val && q.val < cur.val) cur = cur.left;
            else if (p.val > cur.val && q.val > cur.val) cur = cur.right;
            else return cur;
        }
        return null;
    }
    public static void main(String[] args) {
        TreeNode p = new TreeNode(2), q = new TreeNode(8), r = new TreeNode(6);
        r.left = p; r.right = q;
        System.out.println(new __CLASS__().lowestCommonAncestor(r, p, q).val);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left,*right; TreeNode(int v):val(v),left(0),right(0){} };
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        auto* cur = root;
        while (cur) {
            if (p->val < cur->val && q->val < cur->val) cur = cur->left;
            else if (p->val > cur->val && q->val > cur->val) cur = cur->right;
            else return cur;
        }
        return nullptr;
    }
};
int main() {
    auto* p = new TreeNode(2); auto* q = new TreeNode(8);
    auto* r = new TreeNode(6); r->left = p; r->right = q;
    cout << Solution().lowestCommonAncestor(r,p,q)->val << endl;
}
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    cur := root
    for cur != nil {
        if p.Val < cur.Val && q.Val < cur.Val { cur = cur.Left
        } else if p.Val > cur.Val && q.Val > cur.Val { cur = cur.Right
        } else { return cur }
    }
    return nil
}
func main() {
    p := &TreeNode{Val:2}; q := &TreeNode{Val:8}
    r := &TreeNode{Val:6, Left:p, Right:q}
    fmt.Println(lowestCommonAncestor(r,p,q).Val)
}
''',
"R":'''
lowestCommonAncestor <- function(root, p, q) {
    cur <- root
    while (!is.null(cur)) {
        if (p < cur$val && q < cur$val) cur <- cur$left
        else if (p > cur$val && q > cur$val) cur <- cur$right
        else return(cur$val)
    }
    NA
}
root <- list(val=6,
             left=list(val=2, left=NULL, right=NULL),
             right=list(val=8, left=NULL, right=NULL))
print(lowestCommonAncestor(root, 2, 8))  # 6
''',
}))

# 015 - Excel Sheet Column Title
LESSONS.append((15, "Excel Sheet Column Title", "Math and Geometry", "Easy", 8,
"""Given an integer columnNumber, return its corresponding column title
as it appears in an Excel sheet.

Example:
  1  -> A
  28 -> AB
  701 -> ZY""",
{
"Python":'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        out = []
        while n:
            n -= 1
            out.append(chr(ord('A') + n % 26))
            n //= 26
        return "".join(reversed(out))

if __name__ == "__main__":
    print(Solution().convertToTitle(1), Solution().convertToTitle(28), Solution().convertToTitle(701))
''',
"JavaScript":'''
var convertToTitle = function(n) {
    let out = "";
    while (n > 0) { n--; out = String.fromCharCode(65 + n % 26) + out; n = Math.floor(n / 26); }
    return out;
};
console.log(convertToTitle(1), convertToTitle(28), convertToTitle(701));
''',
"Java":'''
public class __CLASS__ {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) { n--; sb.append((char)('A' + n % 26)); n /= 26; }
        return sb.reverse().toString();
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.convertToTitle(1) + " " + s.convertToTitle(28) + " " + s.convertToTitle(701));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string convertToTitle(int n) {
        string out;
        while (n > 0) { --n; out += char('A' + n % 26); n /= 26; }
        reverse(out.begin(), out.end());
        return out;
    }
};
int main() {
    Solution s;
    cout << s.convertToTitle(1) << " " << s.convertToTitle(28) << " " << s.convertToTitle(701) << endl;
}
''',
"Go":'''
package main
import "fmt"
func convertToTitle(n int) string {
    out := []byte{}
    for n > 0 { n--; out = append([]byte{byte('A' + n%26)}, out...); n /= 26 }
    return string(out)
}
func main() { fmt.Println(convertToTitle(1), convertToTitle(28), convertToTitle(701)) }
''',
"R":'''
convertToTitle <- function(n) {
    out <- ""
    while (n > 0) { n <- n - 1; out <- paste0(LETTERS[(n %% 26) + 1], out); n <- n %/% 26 }
    out
}
print(c(convertToTitle(1), convertToTitle(28), convertToTitle(701)))
''',
}))

# 016 - GCD of Strings
LESSONS.append((16, "Greatest Common Divisor of Strings", "Math and Geometry", "Easy", 8,
"""For two strings s and t, we say "t divides s" if s = t + t + ... + t.
Return the largest string x such that x divides both str1 and str2.

Example:
  Input : str1="ABCABC", str2="ABC"     Output: "ABC"
  Input : str1="ABABAB", str2="ABAB"    Output: "AB"
  Input : str1="LEET",   str2="CODE"    Output: ""  """,
{
"Python":'''
from math import gcd
class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 + s2 != s2 + s1: return ""
        return s1[:gcd(len(s1), len(s2))]

if __name__ == "__main__":
    s = Solution()
    print(s.gcdOfStrings("ABCABC","ABC"), s.gcdOfStrings("ABABAB","ABAB"), s.gcdOfStrings("LEET","CODE"))
''',
"JavaScript":'''
const gcd = (a,b) => b ? gcd(b, a % b) : a;
var gcdOfStrings = function(s1, s2) {
    if (s1 + s2 !== s2 + s1) return "";
    return s1.slice(0, gcd(s1.length, s2.length));
};
console.log(gcdOfStrings("ABCABC","ABC"), gcdOfStrings("ABABAB","ABAB"), gcdOfStrings("LEET","CODE"));
''',
"Java":'''
public class __CLASS__ {
    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    public String gcdOfStrings(String s1, String s2) {
        if (!(s1+s2).equals(s2+s1)) return "";
        return s1.substring(0, gcd(s1.length(), s2.length()));
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.gcdOfStrings("ABCABC","ABC") + "|" + s.gcdOfStrings("ABABAB","ABAB") + "|" + s.gcdOfStrings("LEET","CODE"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string gcdOfStrings(string s1, string s2) {
        if (s1 + s2 != s2 + s1) return "";
        return s1.substr(0, __gcd((int)s1.size(), (int)s2.size()));
    }
};
int main() {
    Solution s;
    cout << s.gcdOfStrings("ABCABC","ABC") << "|" << s.gcdOfStrings("ABABAB","ABAB") << "|" << s.gcdOfStrings("LEET","CODE") << endl;
}
''',
"Go":'''
package main
import "fmt"
func gcd(a, b int) int { for b != 0 { a, b = b, a%b }; return a }
func gcdOfStrings(s1, s2 string) string {
    if s1+s2 != s2+s1 { return "" }
    return s1[:gcd(len(s1), len(s2))]
}
func main() {
    fmt.Println(gcdOfStrings("ABCABC","ABC"), gcdOfStrings("ABABAB","ABAB"), gcdOfStrings("LEET","CODE"))
}
''',
"R":'''
gcd_int <- function(a,b) { while (b != 0) { t <- b; b <- a %% b; a <- t }; a }
gcdOfStrings <- function(s1, s2) {
    if (paste0(s1,s2) != paste0(s2,s1)) return("")
    substr(s1, 1, gcd_int(nchar(s1), nchar(s2)))
}
print(c(gcdOfStrings("ABCABC","ABC"), gcdOfStrings("ABABAB","ABAB"), gcdOfStrings("LEET","CODE")))
''',
}))

# 017 - Climbing Stairs
LESSONS.append((17, "Climbing Stairs", "1-D Dynamic Programming", "Easy", 9,
"""You are climbing a staircase. It takes n steps to reach the top. Each
time you can climb 1 or 2 steps. In how many distinct ways can you climb
to the top?

Example:
  Input : n = 2  -> 2
  Input : n = 3  -> 3""",
{
"Python":'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n): a, b = b, a + b
        return a

if __name__ == "__main__":
    print(Solution().climbStairs(2), Solution().climbStairs(3), Solution().climbStairs(5))
''',
"JavaScript":'''
var climbStairs = function(n) {
    let a = 1, b = 1;
    for (let i = 0; i < n; i++) [a, b] = [b, a + b];
    return a;
};
console.log(climbStairs(2), climbStairs(3), climbStairs(5));
''',
"Java":'''
public class __CLASS__ {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 0; i < n; i++) { int t = a + b; a = b; b = t; }
        return a;
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.climbStairs(2) + " " + s.climbStairs(3) + " " + s.climbStairs(5));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 0; i < n; ++i) { int t = a + b; a = b; b = t; }
        return a;
    }
};
int main() {
    Solution s;
    cout << s.climbStairs(2) << " " << s.climbStairs(3) << " " << s.climbStairs(5) << endl;
}
''',
"Go":'''
package main
import "fmt"
func climbStairs(n int) int {
    a, b := 1, 1
    for i := 0; i < n; i++ { a, b = b, a+b }
    return a
}
func main() { fmt.Println(climbStairs(2), climbStairs(3), climbStairs(5)) }
''',
"R":'''
climbStairs <- function(n) {
    a <- 1; b <- 1
    for (i in seq_len(n)) { t <- a + b; a <- b; b <- t }
    a
}
print(c(climbStairs(2), climbStairs(3), climbStairs(5)))
''',
}))

# 018 - Min Cost Climbing Stairs
LESSONS.append((18, "Min Cost Climbing Stairs", "1-D Dynamic Programming", "Easy", 9,
"""You are given an integer array cost where cost[i] is the cost of i-th
step. Once you pay the cost, you can either climb one or two steps. You
can start from index 0 or 1. Return the minimum cost to reach the top.

Example:
  Input : cost = [10,15,20]            Output: 15
  Input : cost = [1,100,1,1,1,100,1,1,100,1]   Output: 6""",
{
"Python":'''
class Solution:
    def minCostClimbingStairs(self, cost):
        a = b = 0
        for c in cost: a, b = b, min(a, b) + c
        return min(a, b)

if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]), s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
''',
"JavaScript":'''
var minCostClimbingStairs = function(cost) {
    let a = 0, b = 0;
    for (const c of cost) { const t = Math.min(a, b) + c; a = b; b = t; }
    return Math.min(a, b);
};
console.log(minCostClimbingStairs([10,15,20]), minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]));
''',
"Java":'''
public class __CLASS__ {
    public int minCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        for (int c : cost) { int t = Math.min(a,b) + c; a = b; b = t; }
        return Math.min(a, b);
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.minCostClimbingStairs(new int[]{10,15,20}) + " " +
                           s.minCostClimbingStairs(new int[]{1,100,1,1,1,100,1,1,100,1}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int a = 0, b = 0;
        for (int c : cost) { int t = min(a,b) + c; a = b; b = t; }
        return min(a, b);
    }
};
int main() {
    Solution s;
    vector<int> v1 = {10,15,20}, v2 = {1,100,1,1,1,100,1,1,100,1};
    cout << s.minCostClimbingStairs(v1) << " " << s.minCostClimbingStairs(v2) << endl;
}
''',
"Go":'''
package main
import "fmt"
func minCostClimbingStairs(cost []int) int {
    a, b := 0, 0
    for _, c := range cost { t := a; if b < t { t = b }; a = b; b = t + c }
    if a < b { return a }
    return b
}
func main() {
    fmt.Println(minCostClimbingStairs([]int{10,15,20}), minCostClimbingStairs([]int{1,100,1,1,1,100,1,1,100,1}))
}
''',
"R":'''
minCostClimbingStairs <- function(cost) {
    a <- 0; b <- 0
    for (c in cost) { t <- min(a,b) + c; a <- b; b <- t }
    min(a,b)
}
print(c(minCostClimbingStairs(c(10,15,20)),
        minCostClimbingStairs(c(1,100,1,1,1,100,1,1,100,1))))
''',
}))

# 019 - Kth Largest Element In a Stream
LESSONS.append((19, "Kth Largest Element In a Stream", "Heap Priority Queue", "Easy", 10,
"""Design a class to find the kth largest element in a stream. Implement:
  KthLargest(int k, int[] nums)
  add(val) -> returns the element representing the kth largest in the stream.

Example:
  k=3, nums=[4,5,8,2]
  add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8""",
{
"Python":'''
import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k; self.h = nums[:]
        heapq.heapify(self.h)
        while len(self.h) > k: heapq.heappop(self.h)
    def add(self, val):
        heapq.heappush(self.h, val)
        if len(self.h) > self.k: heapq.heappop(self.h)
        return self.h[0]

if __name__ == "__main__":
    kl = KthLargest(3, [4,5,8,2])
    print([kl.add(x) for x in [3,5,10,9,4]])  # [4,5,5,8,8]
''',
"JavaScript":'''
// min-heap of size k
class KthLargest {
    constructor(k, nums) { this.k = k; this.h = []; for (const n of nums) this.add(n); }
    add(val) {
        if (this.h.length < this.k) { this._push(val); }
        else if (val > this.h[0]) { this.h[0] = val; this._down(0); }
        return this.h[0];
    }
    _push(v) { this.h.push(v); this._up(this.h.length - 1); }
    _up(i) { while (i > 0) { const p = (i-1)>>1; if (this.h[p] > this.h[i]) { [this.h[p],this.h[i]]=[this.h[i],this.h[p]]; i = p; } else break; } }
    _down(i) { const n = this.h.length; while (true) { const l=2*i+1, r=2*i+2; let s=i;
        if (l<n && this.h[l]<this.h[s]) s=l; if (r<n && this.h[r]<this.h[s]) s=r;
        if (s===i) break; [this.h[s],this.h[i]]=[this.h[i],this.h[s]]; i=s; } }
}
const kl = new KthLargest(3, [4,5,8,2]);
console.log([3,5,10,9,4].map(x => kl.add(x)));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class KthLargest {
        PriorityQueue<Integer> pq; int k;
        public KthLargest(int k, int[] nums) {
            this.k = k; pq = new PriorityQueue<>();
            for (int n : nums) add(n);
        }
        public int add(int val) {
            if (pq.size() < k) pq.offer(val);
            else if (val > pq.peek()) { pq.poll(); pq.offer(val); }
            return pq.peek();
        }
    }
    public static void main(String[] args) {
        KthLargest kl = new KthLargest(3, new int[]{4,5,8,2});
        for (int x : new int[]{3,5,10,9,4}) System.out.print(kl.add(x) + " ");
        System.out.println();
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
public:
    KthLargest(int k, vector<int>& nums) : k(k) { for (int n : nums) add(n); }
    int add(int val) {
        if ((int)pq.size() < k) pq.push(val);
        else if (val > pq.top()) { pq.pop(); pq.push(val); }
        return pq.top();
    }
};
int main() {
    vector<int> v = {4,5,8,2}; KthLargest kl(3, v);
    for (int x : {3,5,10,9,4}) cout << kl.add(x) << " ";
    cout << endl;
}
''',
"Go":'''
package main
import ("container/heap"; "fmt")
type IntHeap []int
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i,j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i,j int) { h[i],h[j] = h[j],h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type KthLargest struct { h *IntHeap; k int }
func Constructor(k int, nums []int) KthLargest {
    h := &IntHeap{}; heap.Init(h)
    kl := KthLargest{h, k}
    for _, n := range nums { kl.Add(n) }
    return kl
}
func (kl *KthLargest) Add(val int) int {
    if kl.h.Len() < kl.k { heap.Push(kl.h, val)
    } else if val > (*kl.h)[0] { heap.Pop(kl.h); heap.Push(kl.h, val) }
    return (*kl.h)[0]
}

func main() {
    kl := Constructor(3, []int{4,5,8,2})
    for _, x := range []int{3,5,10,9,4} { fmt.Print(kl.Add(x), " ") }
    fmt.Println()
}
''',
"R":'''
# Maintain a sorted vector of size <= k.
KthLargest <- function(k, nums) {
    e <- new.env(); e$k <- k; e$h <- sort(nums, decreasing=TRUE)
    if (length(e$h) > k) e$h <- e$h[1:k]
    e
}
add_kl <- function(e, val) {
    e$h <- sort(c(e$h, val), decreasing=TRUE)
    if (length(e$h) > e$k) e$h <- e$h[1:e$k]
    e$h[e$k]
}
kl <- KthLargest(3, c(4,5,8,2))
print(sapply(c(3,5,10,9,4), function(x) add_kl(kl, x)))
''',
}))

# 020 - K Closest Points to Origin
LESSONS.append((20, "K Closest Points to Origin", "Heap Priority Queue", "Medium", 10,
"""Given an array of points where points[i] = [xi, yi] and an integer k,
return the k closest points to the origin (0, 0). Distance is Euclidean.

Example:
  Input : points = [[1,3],[-2,2]], k = 1
  Output: [[-2,2]]""",
{
"Python":'''
import heapq
class Solution:
    def kClosest(self, points, k):
        h = []
        for x, y in points:
            heapq.heappush(h, (-(x*x + y*y), [x,y]))
            if len(h) > k: heapq.heappop(h)
        return [p for _, p in h]

if __name__ == "__main__":
    print(Solution().kClosest([[1,3],[-2,2]], 1))
    print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
''',
"JavaScript":'''
var kClosest = function(points, k) {
    return points.slice().sort((a,b) => (a[0]**2+a[1]**2) - (b[0]**2+b[1]**2)).slice(0, k);
};
console.log(kClosest([[1,3],[-2,2]], 1));
console.log(kClosest([[3,3],[5,-1],[-2,4]], 2));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) ->
            (b[0]*b[0]+b[1]*b[1]) - (a[0]*a[0]+a[1]*a[1]));
        for (int[] p : points) { pq.offer(p); if (pq.size() > k) pq.poll(); }
        int[][] out = new int[k][];
        for (int i = 0; i < k; i++) out[i] = pq.poll();
        return out;
    }
    public static void main(String[] args) {
        int[][] r = new __CLASS__().kClosest(new int[][]{{3,3},{5,-1},{-2,4}}, 2);
        for (int[] p : r) System.out.println(p[0] + "," + p[1]);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> pq;
        for (auto& p : points) {
            int d = p[0]*p[0] + p[1]*p[1];
            pq.push({d, p});
            if ((int)pq.size() > k) pq.pop();
        }
        vector<vector<int>> out;
        while (!pq.empty()) { out.push_back(pq.top().second); pq.pop(); }
        return out;
    }
};
int main() {
    vector<vector<int>> v = {{3,3},{5,-1},{-2,4}};
    for (auto& p : Solution().kClosest(v, 2)) cout << p[0] << "," << p[1] << " ";
    cout << endl;
}
''',
"Go":'''
package main
import ("fmt"; "sort")
func kClosest(points [][]int, k int) [][]int {
    sort.Slice(points, func(i,j int) bool {
        return points[i][0]*points[i][0]+points[i][1]*points[i][1] <
               points[j][0]*points[j][0]+points[j][1]*points[j][1]
    })
    return points[:k]
}
func main() {
    fmt.Println(kClosest([][]int{{1,3},{-2,2}}, 1))
    fmt.Println(kClosest([][]int{{3,3},{5,-1},{-2,4}}, 2))
}
''',
"R":'''
kClosest <- function(points, k) {
    d <- sapply(points, function(p) p[1]^2 + p[2]^2)
    points[order(d)][1:k]
}
print(kClosest(list(c(1,3), c(-2,2)), 1))
print(kClosest(list(c(3,3), c(5,-1), c(-2,4)), 2))
''',
}))

# 021 - Baseball Game
LESSONS.append((21, "Baseball Game", "Stack", "Easy", 11,
"""You are keeping the scores for a baseball game. Operations:
  Integer x : record a new score x
  '+'       : record sum of previous two scores
  'D'       : record double of previous score
  'C'       : invalidate the previous score, removing it
Return the sum of all the scores after all operations.

Example:
  Input : ops = ["5","2","C","D","+"]
  Output: 30   (records: 5, 10, 15)""",
{
"Python":'''
class Solution:
    def calPoints(self, ops):
        st = []
        for op in ops:
            if op == '+': st.append(st[-1] + st[-2])
            elif op == 'D': st.append(2 * st[-1])
            elif op == 'C': st.pop()
            else: st.append(int(op))
        return sum(st)

if __name__ == "__main__":
    print(Solution().calPoints(["5","2","C","D","+"]))  # 30
''',
"JavaScript":'''
var calPoints = function(ops) {
    const st = [];
    for (const o of ops) {
        if (o === '+') st.push(st[st.length-1] + st[st.length-2]);
        else if (o === 'D') st.push(2 * st[st.length-1]);
        else if (o === 'C') st.pop();
        else st.push(parseInt(o, 10));
    }
    return st.reduce((a,b) => a+b, 0);
};
console.log(calPoints(["5","2","C","D","+"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int calPoints(String[] ops) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String o : ops) {
            switch (o) {
                case "+": { int a = st.pop(), b = st.peek(); st.push(a); st.push(a+b); break; }
                case "D": st.push(2 * st.peek()); break;
                case "C": st.pop(); break;
                default:  st.push(Integer.parseInt(o));
            }
        }
        int s = 0; for (int x : st) s += x; return s;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().calPoints(new String[]{"5","2","C","D","+"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> st;
        for (auto& o : ops) {
            if (o == "+") st.push_back(st[st.size()-1] + st[st.size()-2]);
            else if (o == "D") st.push_back(2 * st.back());
            else if (o == "C") st.pop_back();
            else st.push_back(stoi(o));
        }
        return accumulate(st.begin(), st.end(), 0);
    }
};
int main() {
    vector<string> v = {"5","2","C","D","+"};
    cout << Solution().calPoints(v) << endl;
}
''',
"Go":'''
package main
import ("fmt"; "strconv")
func calPoints(ops []string) int {
    st := []int{}
    for _, o := range ops {
        switch o {
        case "+": st = append(st, st[len(st)-1]+st[len(st)-2])
        case "D": st = append(st, 2*st[len(st)-1])
        case "C": st = st[:len(st)-1]
        default: n, _ := strconv.Atoi(o); st = append(st, n)
        }
    }
    s := 0; for _, v := range st { s += v }; return s
}
func main() { fmt.Println(calPoints([]string{"5","2","C","D","+"})) }
''',
"R":'''
calPoints <- function(ops) {
    st <- integer(0)
    for (o in ops) {
        if (o == "+") st <- c(st, st[length(st)] + st[length(st)-1])
        else if (o == "D") st <- c(st, 2 * st[length(st)])
        else if (o == "C") st <- st[-length(st)]
        else st <- c(st, as.integer(o))
    }
    sum(st)
}
print(calPoints(c("5","2","C","D","+")))
''',
}))

# 022 - Valid Parentheses
LESSONS.append((22, "Valid Parentheses", "Stack", "Easy", 11,
"""Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid. An input string is
valid if open brackets are closed by the same type of brackets in the
correct order.

Example:
  Input : "()[]{}"   Output: true
  Input : "(]"       Output: false""",
{
"Python":'''
class Solution:
    def isValid(self, s: str) -> bool:
        m = {')':'(', ']':'[', '}':'{'}
        st = []
        for c in s:
            if c in m:
                if not st or st.pop() != m[c]: return False
            else: st.append(c)
        return not st

if __name__ == "__main__":
    print(Solution().isValid("()[]{}"), Solution().isValid("(]"))
''',
"JavaScript":'''
var isValid = function(s) {
    const m = {')':'(', ']':'[', '}':'{'};
    const st = [];
    for (const c of s) {
        if (m[c]) { if (st.pop() !== m[c]) return false; }
        else st.push(c);
    }
    return st.length === 0;
};
console.log(isValid("()[]{}"), isValid("(]"));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean isValid(String s) {
        Map<Character, Character> m = Map.of(')','(', ']','[', '}','{');
        Deque<Character> st = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (m.containsKey(c)) { if (st.isEmpty() || st.pop() != m.get(c)) return false; }
            else st.push(c);
        }
        return st.isEmpty();
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.isValid("()[]{}") + " " + s.isValid("(]"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> m = {{')','('}, {']','['}, {'}','{'}};
        stack<char> st;
        for (char c : s) {
            if (m.count(c)) { if (st.empty() || st.top() != m[c]) return false; st.pop(); }
            else st.push(c);
        }
        return st.empty();
    }
};
int main() {
    Solution s;
    cout << boolalpha << s.isValid("()[]{}") << " " << s.isValid("(]") << endl;
}
''',
"Go":'''
package main
import "fmt"
func isValid(s string) bool {
    m := map[byte]byte{')':'(', ']':'[', '}':'{'}
    st := []byte{}
    for i := 0; i < len(s); i++ {
        c := s[i]
        if op, ok := m[c]; ok {
            if len(st) == 0 || st[len(st)-1] != op { return false }
            st = st[:len(st)-1]
        } else { st = append(st, c) }
    }
    return len(st) == 0
}
func main() { fmt.Println(isValid("()[]{}"), isValid("(]")) }
''',
"R":'''
isValid <- function(s) {
    m <- c(")"="(", "]"="[", "}"="{")
    st <- character(0)
    for (c in strsplit(s, "")[[1]]) {
        if (c %in% names(m)) {
            if (length(st)==0 || st[length(st)] != m[[c]]) return(FALSE)
            st <- st[-length(st)]
        } else st <- c(st, c)
    }
    length(st) == 0
}
print(c(isValid("()[]{}"), isValid("(]")))
''',
}))

# 023 - Extra Characters in a String
LESSONS.append((23, "Extra Characters in a String", "Tries", "Medium", 12,
"""Given a string s and a dictionary of words, break s into one or more
non-overlapping substrings such that each substring is in dictionary.
There may be characters in s that are not in any of the substrings.
Return the minimum number of extra characters left over.

Example:
  Input : s = "leetscode", dict = ["leet","code","leetcode"]
  Output: 1   (the 's' is extra)""",
{
"Python":'''
class Solution:
    def minExtraChar(self, s, dictionary):
        words = set(dictionary); n = len(s)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if s[j:i] in words: dp[i] = min(dp[i], dp[j])
        return dp[n]

if __name__ == "__main__":
    print(Solution().minExtraChar("leetscode", ["leet","code","leetcode"]))  # 1
''',
"JavaScript":'''
var minExtraChar = function(s, dictionary) {
    const words = new Set(dictionary), n = s.length;
    const dp = new Array(n+1).fill(0);
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i-1] + 1;
        for (let j = 0; j < i; j++) if (words.has(s.slice(j,i))) dp[i] = Math.min(dp[i], dp[j]);
    }
    return dp[n];
};
console.log(minExtraChar("leetscode", ["leet","code","leetcode"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int minExtraChar(String s, String[] dictionary) {
        Set<String> words = new HashSet<>(Arrays.asList(dictionary));
        int n = s.length(); int[] dp = new int[n+1];
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1] + 1;
            for (int j = 0; j < i; j++)
                if (words.contains(s.substring(j,i))) dp[i] = Math.min(dp[i], dp[j]);
        }
        return dp[n];
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().minExtraChar("leetscode", new String[]{"leet","code","leetcode"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> words(dictionary.begin(), dictionary.end());
        int n = s.size(); vector<int> dp(n+1, 0);
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i-1] + 1;
            for (int j = 0; j < i; ++j)
                if (words.count(s.substr(j, i-j))) dp[i] = min(dp[i], dp[j]);
        }
        return dp[n];
    }
};
int main() {
    vector<string> d = {"leet","code","leetcode"};
    cout << Solution().minExtraChar("leetscode", d) << endl;
}
''',
"Go":'''
package main
import "fmt"
func minExtraChar(s string, dictionary []string) int {
    words := map[string]bool{}; for _, w := range dictionary { words[w] = true }
    n := len(s); dp := make([]int, n+1)
    for i := 1; i <= n; i++ {
        dp[i] = dp[i-1] + 1
        for j := 0; j < i; j++ {
            if words[s[j:i]] && dp[j] < dp[i] { dp[i] = dp[j] }
        }
    }
    return dp[n]
}
func main() { fmt.Println(minExtraChar("leetscode", []string{"leet","code","leetcode"})) }
''',
"R":'''
minExtraChar <- function(s, dictionary) {
    words <- dictionary; n <- nchar(s)
    dp <- integer(n+1)
    for (i in seq_len(n)) {
        dp[i+1] <- dp[i] + 1
        for (j in 0:(i-1)) {
            sub <- substr(s, j+1, i)
            if (sub %in% words) dp[i+1] <- min(dp[i+1], dp[j+1])
        }
    }
    dp[n+1]
}
print(minExtraChar("leetscode", c("leet","code","leetcode")))
''',
}))

# 024 - Word Search II
LESSONS.append((24, "Word Search II", "Tries", "Hard", 12,
"""Given an m x n board of characters and a list of strings words, return
all words on the board. Each word must be constructed from letters of
sequentially adjacent cells (horizontal/vertical). The same cell may not
be used more than once in a word.

Example:
  board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
  words=["oath","pea","eat","rain"]
  Output: ["oath","eat"]""",
{
"Python":'''
class Solution:
    def findWords(self, board, words):
        trie = {}
        for w in words:
            n = trie
            for c in w: n = n.setdefault(c, {})
            n['#'] = w
        rows, cols = len(board), len(board[0])
        out = set()
        def dfs(r, c, n):
            ch = board[r][c]
            if ch not in n: return
            nxt = n[ch]
            if '#' in nxt: out.add(nxt['#'])
            board[r][c] = '*'
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '*':
                    dfs(nr, nc, nxt)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols): dfs(r, c, trie)
        return list(out)

if __name__ == "__main__":
    b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    print(sorted(Solution().findWords(b, ["oath","pea","eat","rain"])))
''',
"JavaScript":'''
var findWords = function(board, words) {
    const trie = {};
    for (const w of words) { let n = trie; for (const c of w) { n[c] = n[c] || {}; n = n[c]; } n['#'] = w; }
    const R = board.length, C = board[0].length, out = new Set();
    const dfs = (r, c, n) => {
        const ch = board[r][c];
        if (!n[ch]) return;
        const nxt = n[ch];
        if (nxt['#']) out.add(nxt['#']);
        board[r][c] = '*';
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (nr>=0&&nr<R&&nc>=0&&nc<C&&board[nr][nc]!=='*') dfs(nr,nc,nxt);
        }
        board[r][c] = ch;
    };
    for (let r=0;r<R;r++) for (let c=0;c<C;c++) dfs(r,c,trie);
    return [...out];
};
const b = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]];
console.log(findWords(b, ["oath","pea","eat","rain"]).sort());
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class Node { Map<Character,Node> ch = new HashMap<>(); String word; }
    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) { Node n = root; for (char c : w.toCharArray()) n = n.ch.computeIfAbsent(c, k -> new Node()); n.word = w; }
        Set<String> out = new HashSet<>();
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, out);
        return new ArrayList<>(out);
    }
    void dfs(char[][] b, int r, int c, Node n, Set<String> out) {
        char ch = b[r][c];
        Node nxt = n.ch.get(ch); if (nxt == null) return;
        if (nxt.word != null) out.add(nxt.word);
        b[r][c] = '*';
        int[][] D = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int[] d : D) {
            int nr=r+d[0], nc=c+d[1];
            if (nr>=0&&nr<b.length&&nc>=0&&nc<b[0].length&&b[nr][nc]!='*') dfs(b,nr,nc,nxt,out);
        }
        b[r][c] = ch;
    }
    public static void main(String[] args) {
        char[][] b = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
        List<String> r = new __CLASS__().findWords(b, new String[]{"oath","pea","eat","rain"});
        Collections.sort(r); System.out.println(r);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct Node { unordered_map<char, Node*> ch; string word; };
class Solution {
    int R, C;
    void dfs(vector<vector<char>>& b, int r, int c, Node* n, set<string>& out) {
        char ch = b[r][c];
        if (!n->ch.count(ch)) return;
        Node* nxt = n->ch[ch];
        if (!nxt->word.empty()) out.insert(nxt->word);
        b[r][c] = '*';
        int D[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        for (auto& d : D) { int nr=r+d[0], nc=c+d[1];
            if (nr>=0&&nr<R&&nc>=0&&nc<C&&b[nr][nc]!='*') dfs(b,nr,nc,nxt,out); }
        b[r][c] = ch;
    }
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Node* root = new Node();
        for (auto& w : words) { Node* n = root; for (char c : w) { if (!n->ch.count(c)) n->ch[c] = new Node(); n = n->ch[c]; } n->word = w; }
        R = board.size(); C = board[0].size();
        set<string> out;
        for (int r = 0; r < R; ++r) for (int c = 0; c < C; ++c) dfs(board, r, c, root, out);
        return {out.begin(), out.end()};
    }
};
int main() {
    vector<vector<char>> b = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}};
    vector<string> w = {"oath","pea","eat","rain"};
    auto r = Solution().findWords(b, w);
    for (auto& s : r) cout << s << " ";
    cout << endl;
}
''',
"Go":'''
package main
import ("fmt"; "sort")
type Node struct { ch map[byte]*Node; word string }
func newNode() *Node { return &Node{ch: map[byte]*Node{}} }
func findWords(board [][]byte, words []string) []string {
    root := newNode()
    for _, w := range words {
        n := root
        for i := 0; i < len(w); i++ {
            c := w[i]
            if _, ok := n.ch[c]; !ok { n.ch[c] = newNode() }
            n = n.ch[c]
        }
        n.word = w
    }
    R, C := len(board), len(board[0])
    out := map[string]bool{}
    var dfs func(r, c int, n *Node)
    dfs = func(r, c int, n *Node) {
        ch := board[r][c]
        nxt, ok := n.ch[ch]; if !ok { return }
        if nxt.word != "" { out[nxt.word] = true }
        board[r][c] = '*'
        for _, d := range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} {
            nr, nc := r+d[0], c+d[1]
            if nr>=0 && nr<R && nc>=0 && nc<C && board[nr][nc] != '*' { dfs(nr, nc, nxt) }
        }
        board[r][c] = ch
    }
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { dfs(r, c, root) } }
    res := []string{}
    for k := range out { res = append(res, k) }
    sort.Strings(res)
    return res
}
func main() {
    b := [][]byte{[]byte("oaan"), []byte("etae"), []byte("ihkr"), []byte("iflv")}
    fmt.Println(findWords(b, []string{"oath","pea","eat","rain"}))
}
''',
"R":'''
# Recursive DFS with a hash set for words.
findWords <- function(board, words) {
    R <- nrow(board); C <- ncol(board)
    out <- character(0)
    dict <- new.env(hash=TRUE); for (w in words) assign(w, TRUE, envir=dict)
    prefix_set <- new.env(hash=TRUE)
    for (w in words) for (i in seq_len(nchar(w))) assign(substr(w,1,i), TRUE, envir=prefix_set)
    visited <- matrix(FALSE, R, C)
    dfs <- function(r, c, path) {
        if (r<1 || r>R || c<1 || c>C || visited[r,c]) return()
        np <- paste0(path, board[r,c])
        if (!exists(np, envir=prefix_set, inherits=FALSE)) return()
        if (exists(np, envir=dict, inherits=FALSE)) out[[length(out)+1]] <<- np
        visited[r,c] <<- TRUE
        for (d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))) dfs(r+d[1], c+d[2], np)
        visited[r,c] <<- FALSE
    }
    for (r in seq_len(R)) for (c in seq_len(C)) dfs(r, c, "")
    sort(unique(out))
}
b <- matrix(c("o","a","a","n",
              "e","t","a","e",
              "i","h","k","r",
              "i","f","l","v"), nrow=4, byrow=TRUE)
print(findWords(b, c("oath","pea","eat","rain")))
''',
}))

# 025 - Path with Minimum Effort
LESSONS.append((25, "Path with Minimum Effort", "Advanced Graphs", "Medium", 13,
"""Given an m x n grid of heights, find a path from top-left to
bottom-right that minimizes the maximum absolute difference in heights
between consecutive cells along the path.

Example:
  Input : heights = [[1,2,2],[3,8,2],[5,3,5]]
  Output: 2""",
{
"Python":'''
import heapq
class Solution:
    def minimumEffortPath(self, heights):
        R, C = len(heights), len(heights[0])
        dist = [[float('inf')] * C for _ in range(R)]
        dist[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            d, r, c = heapq.heappop(h)
            if r == R-1 and c == C-1: return d
            if d > dist[r][c]: continue
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C:
                    nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heapq.heappush(h, (nd, nr, nc))
        return 0

if __name__ == "__main__":
    print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))  # 2
''',
"JavaScript":'''
// Dijkstra with a simple priority queue using sort (acceptable for small inputs).
var minimumEffortPath = function(heights) {
    const R = heights.length, C = heights[0].length;
    const dist = Array.from({length:R}, () => new Array(C).fill(Infinity));
    dist[0][0] = 0;
    const pq = [[0,0,0]];
    while (pq.length) {
        pq.sort((a,b) => b[0]-a[0]);
        const [d, r, c] = pq.pop();
        if (r === R-1 && c === C-1) return d;
        if (d > dist[r][c]) continue;
        for (const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
            const nr=r+dr, nc=c+dc;
            if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                const nd = Math.max(d, Math.abs(heights[nr][nc]-heights[r][c]));
                if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.push([nd,nr,nc]); }
            }
        }
    }
    return 0;
};
console.log(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int minimumEffortPath(int[][] h) {
        int R = h.length, C = h[0].length;
        int[][] dist = new int[R][C];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);
        pq.offer(new int[]{0,0,0});
        int[][] D = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()) {
            int[] x = pq.poll(); int d = x[0], r = x[1], c = x[2];
            if (r==R-1 && c==C-1) return d;
            if (d > dist[r][c]) continue;
            for (int[] dd : D) {
                int nr=r+dd[0], nc=c+dd[1];
                if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                    int nd = Math.max(d, Math.abs(h[nr][nc]-h[r][c]));
                    if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.offer(new int[]{nd,nr,nc}); }
                }
            }
        }
        return 0;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().minimumEffortPath(new int[][]{{1,2,2},{3,8,2},{5,3,5}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& h) {
        int R = h.size(), C = h[0].size();
        vector<vector<int>> dist(R, vector<int>(C, INT_MAX));
        dist[0][0] = 0;
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
        pq.push({0,0,0});
        int D[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [d, r, c] = pq.top(); pq.pop();
            if (r==R-1 && c==C-1) return d;
            if (d > dist[r][c]) continue;
            for (auto& dd : D) {
                int nr=r+dd[0], nc=c+dd[1];
                if (nr>=0&&nr<R&&nc>=0&&nc<C) {
                    int nd = max(d, abs(h[nr][nc]-h[r][c]));
                    if (nd < dist[nr][nc]) { dist[nr][nc] = nd; pq.push({nd,nr,nc}); }
                }
            }
        }
        return 0;
    }
};
int main() {
    vector<vector<int>> h = {{1,2,2},{3,8,2},{5,3,5}};
    cout << Solution().minimumEffortPath(h) << endl;
}
''',
"Go":'''
package main
import ("container/heap"; "fmt")
type Item struct { d, r, c int }
type PQ []Item
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].d < p[j].d }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(Item)) }
func (p *PQ) Pop() interface{} { o := *p; n := len(o); x := o[n-1]; *p = o[:n-1]; return x }
func abs(x int) int { if x < 0 { return -x }; return x }
func max(a,b int) int { if a > b { return a }; return b }
func minimumEffortPath(h [][]int) int {
    R, C := len(h), len(h[0])
    dist := make([][]int, R); for i := range dist { dist[i] = make([]int, C); for j := range dist[i] { dist[i][j] = 1<<30 } }
    dist[0][0] = 0
    pq := &PQ{{0,0,0}}; heap.Init(pq)
    D := [4][2]int{{1,0},{-1,0},{0,1},{0,-1}}
    for pq.Len() > 0 {
        x := heap.Pop(pq).(Item)
        if x.r == R-1 && x.c == C-1 { return x.d }
        if x.d > dist[x.r][x.c] { continue }
        for _, d := range D {
            nr, nc := x.r+d[0], x.c+d[1]
            if nr>=0 && nr<R && nc>=0 && nc<C {
                nd := max(x.d, abs(h[nr][nc]-h[x.r][x.c]))
                if nd < dist[nr][nc] { dist[nr][nc] = nd; heap.Push(pq, Item{nd,nr,nc}) }
            }
        }
    }
    return 0
}
func main() { fmt.Println(minimumEffortPath([][]int{{1,2,2},{3,8,2},{5,3,5}})) }
''',
"R":'''
minimumEffortPath <- function(h) {
    R <- nrow(h); C <- ncol(h)
    dist <- matrix(Inf, R, C); dist[1,1] <- 0
    # Simple Dijkstra with repeated min scan (small inputs only)
    visited <- matrix(FALSE, R, C)
    for (step in 1:(R*C)) {
        bestD <- Inf; br <- 0; bc <- 0
        for (i in 1:R) for (j in 1:C) if (!visited[i,j] && dist[i,j] < bestD) { bestD <- dist[i,j]; br <- i; bc <- j }
        if (br == 0) break
        if (br == R && bc == C) return(bestD)
        visited[br, bc] <- TRUE
        for (d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))) {
            nr <- br + d[1]; nc <- bc + d[2]
            if (nr>=1 && nr<=R && nc>=1 && nc<=C) {
                nd <- max(bestD, abs(h[nr,nc] - h[br,bc]))
                if (nd < dist[nr,nc]) dist[nr,nc] <- nd
            }
        }
    }
    dist[R, C]
}
print(minimumEffortPath(matrix(c(1,2,2,3,8,2,5,3,5), nrow=3, byrow=TRUE)))
''',
}))

# 026 - Network Delay Time
LESSONS.append((26, "Network Delay Time", "Advanced Graphs", "Medium", 13,
"""You are given a network of n nodes labeled from 1 to n. times[i] =
[u,v,w] means a signal takes w time from u to v. Starting from node k,
return the time it takes for all nodes to receive the signal. If
impossible, return -1.

Example:
  Input : times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
  Output: 2""",
{
"Python":'''
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        for u,v,w in times: g[u].append((v,w))
        dist = {}
        h = [(0, k)]
        while h:
            d, u = heapq.heappop(h)
            if u in dist: continue
            dist[u] = d
            for v, w in g[u]:
                if v not in dist: heapq.heappush(h, (d+w, v))
        if len(dist) < n: return -1
        return max(dist.values())

if __name__ == "__main__":
    print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
''',
"JavaScript":'''
var networkDelayTime = function(times, n, k) {
    const g = new Map();
    for (const [u,v,w] of times) { if (!g.has(u)) g.set(u, []); g.get(u).push([v,w]); }
    const dist = new Map(); const pq = [[0,k]];
    while (pq.length) {
        pq.sort((a,b) => b[0]-a[0]);
        const [d, u] = pq.pop();
        if (dist.has(u)) continue;
        dist.set(u, d);
        for (const [v,w] of (g.get(u) || [])) if (!dist.has(v)) pq.push([d+w, v]);
    }
    if (dist.size < n) return -1;
    return Math.max(...dist.values());
};
console.log(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> g = new HashMap<>();
        for (int[] t : times) g.computeIfAbsent(t[0], x -> new ArrayList<>()).add(new int[]{t[1], t[2]});
        int[] dist = new int[n+1]; Arrays.fill(dist, Integer.MAX_VALUE); dist[k] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);
        pq.offer(new int[]{0, k});
        while (!pq.isEmpty()) {
            int[] x = pq.poll(); int d = x[0], u = x[1];
            if (d > dist[u]) continue;
            for (int[] e : g.getOrDefault(u, Collections.emptyList())) {
                int nd = d + e[1];
                if (nd < dist[e[0]]) { dist[e[0]] = nd; pq.offer(new int[]{nd, e[0]}); }
            }
        }
        int mx = 0;
        for (int i = 1; i <= n; i++) { if (dist[i] == Integer.MAX_VALUE) return -1; mx = Math.max(mx, dist[i]); }
        return mx;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().networkDelayTime(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> g(n+1);
        for (auto& t : times) g[t[0]].push_back({t[1], t[2]});
        vector<int> dist(n+1, INT_MAX); dist[k] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        pq.push({0, k});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto& [v, w] : g[u]) if (d + w < dist[v]) { dist[v] = d + w; pq.push({dist[v], v}); }
        }
        int mx = 0;
        for (int i = 1; i <= n; ++i) { if (dist[i] == INT_MAX) return -1; mx = max(mx, dist[i]); }
        return mx;
    }
};
int main() {
    vector<vector<int>> t = {{2,1,1},{2,3,1},{3,4,1}};
    cout << Solution().networkDelayTime(t, 4, 2) << endl;
}
''',
"Go":'''
package main
import ("container/heap"; "fmt")
type E struct { d, u int }
type PQ []E
func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i,j int) bool { return p[i].d < p[j].d }
func (p PQ) Swap(i,j int) { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(E)) }
func (p *PQ) Pop() interface{} { o := *p; n := len(o); x := o[n-1]; *p = o[:n-1]; return x }
func networkDelayTime(times [][]int, n, k int) int {
    g := make(map[int][][2]int)
    for _, t := range times { g[t[0]] = append(g[t[0]], [2]int{t[1], t[2]}) }
    const INF = 1 << 30
    dist := make([]int, n+1); for i := range dist { dist[i] = INF }
    dist[k] = 0
    pq := &PQ{{0, k}}; heap.Init(pq)
    for pq.Len() > 0 {
        x := heap.Pop(pq).(E)
        if x.d > dist[x.u] { continue }
        for _, e := range g[x.u] {
            nd := x.d + e[1]
            if nd < dist[e[0]] { dist[e[0]] = nd; heap.Push(pq, E{nd, e[0]}) }
        }
    }
    mx := 0
    for i := 1; i <= n; i++ { if dist[i] == INF { return -1 }; if dist[i] > mx { mx = dist[i] } }
    return mx
}
func main() { fmt.Println(networkDelayTime([][]int{{2,1,1},{2,3,1},{3,4,1}}, 4, 2)) }
''',
"R":'''
networkDelayTime <- function(times, n, k) {
    INF <- .Machine$integer.max
    dist <- rep(INF, n); dist[k] <- 0
    visited <- rep(FALSE, n)
    g <- vector("list", n)
    for (t in times) g[[t[1]]] <- c(g[[t[1]]], list(c(t[2], t[3])))
    for (s in 1:n) {
        u <- which.min(ifelse(visited, INF, dist))
        if (dist[u] == INF) return(-1)
        visited[u] <- TRUE
        for (e in g[[u]]) {
            v <- e[1]; w <- e[2]
            if (!visited[v] && dist[u] + w < dist[v]) dist[v] <- dist[u] + w
        }
    }
    if (any(dist == INF)) return(-1)
    max(dist)
}
print(networkDelayTime(list(c(2,1,1), c(2,3,1), c(3,4,1)), 4, 2))
''',
}))

# 027 - Island Perimeter
LESSONS.append((27, "Island Perimeter", "Graphs", "Easy", 14,
"""Given an m x n grid where 1 represents land and 0 water, return the
perimeter of the island (the grid is completely surrounded by water and
there is exactly one island).

Example:
  Input : grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
  Output: 16""",
{
"Python":'''
class Solution:
    def islandPerimeter(self, grid):
        R, C = len(grid), len(grid[0])
        p = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    p += 4
                    if r and grid[r-1][c] == 1: p -= 2
                    if c and grid[r][c-1] == 1: p -= 2
        return p

if __name__ == "__main__":
    print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
''',
"JavaScript":'''
var islandPerimeter = function(grid) {
    const R = grid.length, C = grid[0].length; let p = 0;
    for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) if (grid[r][c] === 1) {
        p += 4;
        if (r && grid[r-1][c] === 1) p -= 2;
        if (c && grid[r][c-1] === 1) p -= 2;
    }
    return p;
};
console.log(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]));
''',
"Java":'''
public class __CLASS__ {
    public int islandPerimeter(int[][] g) {
        int R = g.length, C = g[0].length, p = 0;
        for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) if (g[r][c] == 1) {
            p += 4;
            if (r > 0 && g[r-1][c] == 1) p -= 2;
            if (c > 0 && g[r][c-1] == 1) p -= 2;
        }
        return p;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().islandPerimeter(new int[][]{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& g) {
        int R = g.size(), C = g[0].size(), p = 0;
        for (int r = 0; r < R; ++r) for (int c = 0; c < C; ++c) if (g[r][c] == 1) {
            p += 4;
            if (r > 0 && g[r-1][c] == 1) p -= 2;
            if (c > 0 && g[r][c-1] == 1) p -= 2;
        }
        return p;
    }
};
int main() {
    vector<vector<int>> g = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    cout << Solution().islandPerimeter(g) << endl;
}
''',
"Go":'''
package main
import "fmt"
func islandPerimeter(g [][]int) int {
    R, C, p := len(g), len(g[0]), 0
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { if g[r][c] == 1 {
        p += 4
        if r > 0 && g[r-1][c] == 1 { p -= 2 }
        if c > 0 && g[r][c-1] == 1 { p -= 2 }
    } } }
    return p
}
func main() { fmt.Println(islandPerimeter([][]int{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}})) }
''',
"R":'''
islandPerimeter <- function(g) {
    R <- nrow(g); C <- ncol(g); p <- 0
    for (r in seq_len(R)) for (c in seq_len(C)) if (g[r,c] == 1) {
        p <- p + 4
        if (r > 1 && g[r-1, c] == 1) p <- p - 2
        if (c > 1 && g[r, c-1] == 1) p <- p - 2
    }
    p
}
print(islandPerimeter(matrix(c(0,1,0,0, 1,1,1,0, 0,1,0,0, 1,1,0,0), nrow=4, byrow=TRUE)))
''',
}))

# 028 - Verifying An Alien Dictionary
LESSONS.append((28, "Verifying An Alien Dictionary", "Graphs", "Easy", 14,
"""In an alien language, surprisingly, they also use English lowercase
letters but possibly in a different order. Given a sequence of words
written in the alien language and the order of the alphabet, return true
iff the given words are sorted lexicographically in this alien language.

Example:
  Input : words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
  Output: true""",
{
"Python":'''
class Solution:
    def isAlienSorted(self, words, order):
        idx = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for ca, cb in zip(a, b):
                if idx[ca] != idx[cb]:
                    if idx[ca] > idx[cb]: return False
                    break
            else:
                if len(a) > len(b): return False
        return True

if __name__ == "__main__":
    print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
''',
"JavaScript":'''
var isAlienSorted = function(words, order) {
    const idx = {}; for (let i = 0; i < order.length; i++) idx[order[i]] = i;
    for (let w = 1; w < words.length; w++) {
        const a = words[w-1], b = words[w]; let ok = false;
        for (let i = 0; i < Math.min(a.length, b.length); i++) {
            if (idx[a[i]] !== idx[b[i]]) { if (idx[a[i]] > idx[b[i]]) return false; ok = true; break; }
        }
        if (!ok && a.length > b.length) return false;
    }
    return true;
};
console.log(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"));
''',
"Java":'''
public class __CLASS__ {
    public boolean isAlienSorted(String[] words, String order) {
        int[] idx = new int[26];
        for (int i = 0; i < 26; i++) idx[order.charAt(i)-'a'] = i;
        for (int w = 1; w < words.length; w++) {
            String a = words[w-1], b = words[w]; boolean broke = false;
            int n = Math.min(a.length(), b.length());
            for (int i = 0; i < n; i++) {
                int ia = idx[a.charAt(i)-'a'], ib = idx[b.charAt(i)-'a'];
                if (ia != ib) { if (ia > ib) return false; broke = true; break; }
            }
            if (!broke && a.length() > b.length()) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().isAlienSorted(new String[]{"hello","leetcode"}, "hlabcdefgijkmnopqrstuvwxyz"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int idx[26]; for (int i = 0; i < 26; ++i) idx[order[i]-'a'] = i;
        for (int w = 1; w < (int)words.size(); ++w) {
            const string& a = words[w-1]; const string& b = words[w]; bool broke = false;
            int n = min(a.size(), b.size());
            for (int i = 0; i < n; ++i) {
                int ia = idx[a[i]-'a'], ib = idx[b[i]-'a'];
                if (ia != ib) { if (ia > ib) return false; broke = true; break; }
            }
            if (!broke && a.size() > b.size()) return false;
        }
        return true;
    }
};
int main() {
    vector<string> v = {"hello","leetcode"};
    cout << boolalpha << Solution().isAlienSorted(v, "hlabcdefgijkmnopqrstuvwxyz") << endl;
}
''',
"Go":'''
package main
import "fmt"
func isAlienSorted(words []string, order string) bool {
    idx := [26]int{}; for i := 0; i < 26; i++ { idx[order[i]-'a'] = i }
    for w := 1; w < len(words); w++ {
        a, b := words[w-1], words[w]; broke := false
        n := len(a); if len(b) < n { n = len(b) }
        for i := 0; i < n; i++ {
            ia, ib := idx[a[i]-'a'], idx[b[i]-'a']
            if ia != ib { if ia > ib { return false }; broke = true; break }
        }
        if !broke && len(a) > len(b) { return false }
    }
    return true
}
func main() { fmt.Println(isAlienSorted([]string{"hello","leetcode"}, "hlabcdefgijkmnopqrstuvwxyz")) }
''',
"R":'''
isAlienSorted <- function(words, order) {
    chars <- strsplit(order, "")[[1]]
    idx <- setNames(seq_along(chars), chars)
    cmp <- function(a, b) {
        n <- min(nchar(a), nchar(b))
        for (i in seq_len(n)) {
            ia <- idx[[substr(a,i,i)]]; ib <- idx[[substr(b,i,i)]]
            if (ia != ib) return(ia - ib)
        }
        nchar(a) - nchar(b)
    }
    for (w in 2:length(words)) if (cmp(words[w-1], words[w]) > 0) return(FALSE)
    TRUE
}
print(isAlienSorted(c("hello","leetcode"), "hlabcdefgijkmnopqrstuvwxyz"))
''',
}))

# 029 - Invert Binary Tree
LESSONS.append((29, "Invert Binary Tree", "Trees", "Easy", 15,
"""Given the root of a binary tree, invert the tree (mirror it), and
return its root.

Example:
  Input : [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r

class Solution:
    def invertTree(self, root):
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def lvl(r):
    out, q = [], [r]
    while q:
        n = q.pop(0)
        if n: out.append(n.val); q.append(n.left); q.append(n.right)
        else: out.append(None)
    while out and out[-1] is None: out.pop()
    return out

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(lvl(Solution().invertTree(root)))
''',
"JavaScript":'''
function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var invertTree = function(root) {
    if (!root) return null;
    [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
    return root;
};
const r = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7, new TreeNode(6), new TreeNode(9)));
const inv = invertTree(r);
console.log(inv.val, inv.left.val, inv.right.val);
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode l = invertTree(root.right), r = invertTree(root.left);
        root.left = l; root.right = r; return root;
    }
    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2); root.left.left = new TreeNode(1); root.left.right = new TreeNode(3);
        root.right = new TreeNode(7); root.right.left = new TreeNode(6); root.right.right = new TreeNode(9);
        TreeNode r = new __CLASS__().invertTree(root);
        System.out.println(r.val + " " + r.left.val + " " + r.right.val);
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left,*right; TreeNode(int v):val(v),left(0),right(0){} };
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        auto* l = invertTree(root->right); auto* r = invertTree(root->left);
        root->left = l; root->right = r; return root;
    }
};
int main() {
    auto* r = new TreeNode(4);
    r->left = new TreeNode(2); r->left->left = new TreeNode(1); r->left->right = new TreeNode(3);
    r->right = new TreeNode(7); r->right->left = new TreeNode(6); r->right->right = new TreeNode(9);
    auto* inv = Solution().invertTree(r);
    cout << inv->val << " " << inv->left->val << " " << inv->right->val << endl;
}
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func invertTree(root *TreeNode) *TreeNode {
    if root == nil { return nil }
    l := invertTree(root.Right); r := invertTree(root.Left)
    root.Left = l; root.Right = r
    return root
}
func main() {
    r := &TreeNode{Val:4,
        Left: &TreeNode{Val:2, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:3}},
        Right:&TreeNode{Val:7, Left:&TreeNode{Val:6}, Right:&TreeNode{Val:9}}}
    inv := invertTree(r)
    fmt.Println(inv.Val, inv.Left.Val, inv.Right.Val)
}
''',
"R":'''
invertTree <- function(node) {
    if (is.null(node)) return(NULL)
    list(val=node$val, left=invertTree(node$right), right=invertTree(node$left))
}
root <- list(val=4,
             left=list(val=2, left=list(val=1,left=NULL,right=NULL), right=list(val=3,left=NULL,right=NULL)),
             right=list(val=7, left=list(val=6,left=NULL,right=NULL), right=list(val=9,left=NULL,right=NULL)))
inv <- invertTree(root)
print(c(inv$val, inv$left$val, inv$right$val))
''',
}))

# 030 - Maximum Depth of Binary Tree
LESSONS.append((30, "Maximum Depth of Binary Tree", "Trees", "Easy", 15,
"""Given the root of a binary tree, return its maximum depth (number of
nodes along the longest path from the root down to the farthest leaf).

Example:
  Input : [3,9,20,null,null,15,7]
  Output: 3""",
{
"Python":'''
class TreeNode:
    def __init__(self, v=0, l=None, r=None): self.val, self.left, self.right = v, l, r
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxDepth(root))  # 3
''',
"JavaScript":'''
function TreeNode(v,l,r){this.val=v??0;this.left=l??null;this.right=r??null;}
var maxDepth = function(root) {
    if (!root) return 0;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};
console.log(maxDepth(new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)))));
''',
"Java":'''
public class __CLASS__ {
    static class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
    public static void main(String[] args) {
        TreeNode r = new TreeNode(3); r.left = new TreeNode(9);
        r.right = new TreeNode(20); r.right.left = new TreeNode(15); r.right.right = new TreeNode(7);
        System.out.println(new __CLASS__().maxDepth(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct TreeNode { int val; TreeNode *left,*right; TreeNode(int v):val(v),left(0),right(0){} };
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
int main() {
    auto* r = new TreeNode(3); r->left = new TreeNode(9);
    r->right = new TreeNode(20); r->right->left = new TreeNode(15); r->right->right = new TreeNode(7);
    cout << Solution().maxDepth(r) << endl;
}
''',
"Go":'''
package main
import "fmt"
type TreeNode struct { Val int; Left,Right *TreeNode }
func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    l := maxDepth(root.Left); r := maxDepth(root.Right)
    if l > r { return 1 + l }; return 1 + r
}
func main() {
    r := &TreeNode{Val:3, Left:&TreeNode{Val:9},
        Right:&TreeNode{Val:20, Left:&TreeNode{Val:15}, Right:&TreeNode{Val:7}}}
    fmt.Println(maxDepth(r))
}
''',
"R":'''
maxDepth <- function(node) {
    if (is.null(node)) return(0)
    1 + max(maxDepth(node$left), maxDepth(node$right))
}
root <- list(val=3,
             left=list(val=9, left=NULL, right=NULL),
             right=list(val=20, left=list(val=15,left=NULL,right=NULL), right=list(val=7,left=NULL,right=NULL)))
print(maxDepth(root))
''',
}))

# 031 - Unique Paths
LESSONS.append((31, "Unique Paths", "2-D Dynamic Programming", "Medium", 16,
"""A robot is on an m x n grid at the top-left. It can only move right or
down. How many possible unique paths are there to reach the bottom-right?

Example:
  Input : m=3, n=7  Output: 28
  Input : m=3, n=2  Output: 3""",
{
"Python":'''
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n): dp[j] += dp[j-1]
        return dp[-1]

if __name__ == "__main__":
    print(Solution().uniquePaths(3,7), Solution().uniquePaths(3,2))
''',
"JavaScript":'''
var uniquePaths = function(m, n) {
    const dp = new Array(n).fill(1);
    for (let i = 1; i < m; i++) for (let j = 1; j < n; j++) dp[j] += dp[j-1];
    return dp[n-1];
};
console.log(uniquePaths(3,7), uniquePaths(3,2));
''',
"Java":'''
public class __CLASS__ {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n]; java.util.Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) for (int j = 1; j < n; j++) dp[j] += dp[j-1];
        return dp[n-1];
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.uniquePaths(3,7) + " " + s.uniquePaths(3,2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; ++i) for (int j = 1; j < n; ++j) dp[j] += dp[j-1];
        return dp[n-1];
    }
};
int main() { Solution s; cout << s.uniquePaths(3,7) << " " << s.uniquePaths(3,2) << endl; }
''',
"Go":'''
package main
import "fmt"
func uniquePaths(m, n int) int {
    dp := make([]int, n); for i := range dp { dp[i] = 1 }
    for i := 1; i < m; i++ { for j := 1; j < n; j++ { dp[j] += dp[j-1] } }
    return dp[n-1]
}
func main() { fmt.Println(uniquePaths(3,7), uniquePaths(3,2)) }
''',
"R":'''
uniquePaths <- function(m, n) {
    dp <- rep(1, n)
    if (m > 1) for (i in 2:m) for (j in 2:n) dp[j] <- dp[j] + dp[j-1]
    dp[n]
}
print(c(uniquePaths(3,7), uniquePaths(3,2)))
''',
}))

# 032 - Unique Paths II
LESSONS.append((32, "Unique Paths II", "2-D Dynamic Programming", "Medium", 16,
"""You are given an m x n integer array obstacleGrid. There is a robot
at the top-left. It moves right or down. An obstacle is marked as 1; an
empty space as 0. Return the number of possible unique paths to the
bottom-right corner.

Example:
  Input : [[0,0,0],[0,1,0],[0,0,0]]   Output: 2""",
{
"Python":'''
class Solution:
    def uniquePathsWithObstacles(self, g):
        R, C = len(g), len(g[0])
        if g[0][0] == 1: return 0
        dp = [0] * C; dp[0] = 1
        for r in range(R):
            if g[r][0] == 1: dp[0] = 0
            for c in range(1, C):
                dp[c] = 0 if g[r][c] == 1 else dp[c] + dp[c-1]
        return dp[-1]

if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2
''',
"JavaScript":'''
var uniquePathsWithObstacles = function(g) {
    const R = g.length, C = g[0].length;
    if (g[0][0] === 1) return 0;
    const dp = new Array(C).fill(0); dp[0] = 1;
    for (let r = 0; r < R; r++) {
        if (g[r][0] === 1) dp[0] = 0;
        for (let c = 1; c < C; c++) dp[c] = g[r][c] === 1 ? 0 : dp[c] + dp[c-1];
    }
    return dp[C-1];
};
console.log(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]));
''',
"Java":'''
public class __CLASS__ {
    public int uniquePathsWithObstacles(int[][] g) {
        int R = g.length, C = g[0].length;
        if (g[0][0] == 1) return 0;
        int[] dp = new int[C]; dp[0] = 1;
        for (int r = 0; r < R; r++) {
            if (g[r][0] == 1) dp[0] = 0;
            for (int c = 1; c < C; c++) dp[c] = g[r][c] == 1 ? 0 : dp[c] + dp[c-1];
        }
        return dp[C-1];
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().uniquePathsWithObstacles(new int[][]{{0,0,0},{0,1,0},{0,0,0}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& g) {
        int R = g.size(), C = g[0].size();
        if (g[0][0]) return 0;
        vector<long long> dp(C, 0); dp[0] = 1;
        for (int r = 0; r < R; ++r) {
            if (g[r][0]) dp[0] = 0;
            for (int c = 1; c < C; ++c) dp[c] = g[r][c] ? 0 : dp[c] + dp[c-1];
        }
        return (int)dp[C-1];
    }
};
int main() {
    vector<vector<int>> g = {{0,0,0},{0,1,0},{0,0,0}};
    cout << Solution().uniquePathsWithObstacles(g) << endl;
}
''',
"Go":'''
package main
import "fmt"
func uniquePathsWithObstacles(g [][]int) int {
    R, C := len(g), len(g[0])
    if g[0][0] == 1 { return 0 }
    dp := make([]int, C); dp[0] = 1
    for r := 0; r < R; r++ {
        if g[r][0] == 1 { dp[0] = 0 }
        for c := 1; c < C; c++ { if g[r][c] == 1 { dp[c] = 0 } else { dp[c] += dp[c-1] } }
    }
    return dp[C-1]
}
func main() { fmt.Println(uniquePathsWithObstacles([][]int{{0,0,0},{0,1,0},{0,0,0}})) }
''',
"R":'''
uniquePathsWithObstacles <- function(g) {
    R <- nrow(g); C <- ncol(g)
    if (g[1,1] == 1) return(0)
    dp <- integer(C); dp[1] <- 1
    for (r in 1:R) {
        if (g[r,1] == 1) dp[1] <- 0
        if (C > 1) for (c in 2:C) dp[c] <- if (g[r,c] == 1) 0 else dp[c] + dp[c-1]
    }
    dp[C]
}
print(uniquePathsWithObstacles(matrix(c(0,0,0, 0,1,0, 0,0,0), nrow=3, byrow=TRUE)))
''',
}))

# 033 - Last Stone Weight
LESSONS.append((33, "Last Stone Weight", "Heap Priority Queue", "Easy", 17,
"""You are given an array of stones. On each turn pick the two heaviest
stones x <= y. If x == y both are destroyed; if x != y, x is destroyed
and y becomes y - x. Return the weight of the last remaining stone (or 0).

Example:
  Input : [2,7,4,1,8,1]   Output: 1""",
{
"Python":'''
import heapq
class Solution:
    def lastStoneWeight(self, stones):
        h = [-s for s in stones]; heapq.heapify(h)
        while len(h) > 1:
            y = -heapq.heappop(h); x = -heapq.heappop(h)
            if y != x: heapq.heappush(h, -(y - x))
        return -h[0] if h else 0

if __name__ == "__main__":
    print(Solution().lastStoneWeight([2,7,4,1,8,1]))  # 1
''',
"JavaScript":'''
var lastStoneWeight = function(stones) {
    const a = stones.slice();
    while (a.length > 1) {
        a.sort((x,y) => x-y);
        const y = a.pop(), x = a.pop();
        if (y !== x) a.push(y - x);
    }
    return a[0] ?? 0;
};
console.log(lastStoneWeight([2,7,4,1,8,1]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int s : stones) pq.offer(s);
        while (pq.size() > 1) {
            int y = pq.poll(), x = pq.poll();
            if (y != x) pq.offer(y - x);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().lastStoneWeight(new int[]{2,7,4,1,8,1}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1) {
            int y = pq.top(); pq.pop(); int x = pq.top(); pq.pop();
            if (y != x) pq.push(y - x);
        }
        return pq.empty() ? 0 : pq.top();
    }
};
int main() {
    vector<int> v = {2,7,4,1,8,1};
    cout << Solution().lastStoneWeight(v) << endl;
}
''',
"Go":'''
package main
import ("container/heap"; "fmt")
type IH []int
func (h IH) Len() int { return len(h) }
func (h IH) Less(i,j int) bool { return h[i] > h[j] }
func (h IH) Swap(i,j int) { h[i], h[j] = h[j], h[i] }
func (h *IH) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IH) Pop() interface{} { o := *h; n := len(o); x := o[n-1]; *h = o[:n-1]; return x }
func lastStoneWeight(stones []int) int {
    h := IH(append([]int{}, stones...)); heap.Init(&h)
    for h.Len() > 1 {
        y := heap.Pop(&h).(int); x := heap.Pop(&h).(int)
        if y != x { heap.Push(&h, y-x) }
    }
    if h.Len() == 0 { return 0 }
    return h[0]
}
func main() { fmt.Println(lastStoneWeight([]int{2,7,4,1,8,1})) }
''',
"R":'''
lastStoneWeight <- function(stones) {
    s <- stones
    while (length(s) > 1) {
        s <- sort(s)
        y <- s[length(s)]; x <- s[length(s)-1]
        s <- s[-c(length(s), length(s)-1)]
        if (y != x) s <- c(s, y - x)
    }
    if (length(s) == 0) 0L else s[1]
}
print(lastStoneWeight(c(2,7,4,1,8,1)))
''',
}))

# 034 - Kth Largest Element In An Array
LESSONS.append((34, "Kth Largest Element In An Array", "Heap Priority Queue", "Medium", 17,
"""Given an integer array nums and an integer k, return the kth largest
element in the array (the kth largest in sorted order, not the kth
distinct element).

Example:
  Input : [3,2,1,5,6,4], k=2   Output: 5""",
{
"Python":'''
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # 5
''',
"JavaScript":'''
var findKthLargest = function(nums, k) {
    return nums.slice().sort((a,b) => b-a)[k-1];
};
console.log(findKthLargest([3,2,1,5,6,4], 2));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n : nums) { pq.offer(n); if (pq.size() > k) pq.poll(); }
        return pq.peek();
    }
    public static void main(String[] args) {
        System.out.println(new __CLASS__().findKthLargest(new int[]{3,2,1,5,6,4}, 2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<>> pq;
        for (int n : nums) { pq.push(n); if ((int)pq.size() > k) pq.pop(); }
        return pq.top();
    }
};
int main() {
    vector<int> v = {3,2,1,5,6,4};
    cout << Solution().findKthLargest(v, 2) << endl;
}
''',
"Go":'''
package main
import ("fmt"; "sort")
func findKthLargest(nums []int, k int) int {
    a := append([]int{}, nums...)
    sort.Sort(sort.Reverse(sort.IntSlice(a)))
    return a[k-1]
}
func main() { fmt.Println(findKthLargest([]int{3,2,1,5,6,4}, 2)) }
''',
"R":'''
findKthLargest <- function(nums, k) sort(nums, decreasing=TRUE)[k]
print(findKthLargest(c(3,2,1,5,6,4), 2))
''',
}))

# 035 - Sum of All Subsets XOR Total
LESSONS.append((35, "Sum of All Subsets XOR Total", "Backtracking", "Easy", 18,
"""The XOR total of an array is the bitwise XOR of all its elements (or 0
if empty). Return the sum of all XOR totals for every subset of nums.

Example:
  Input : [1,3]      Output: 6   (subsets: [],[1],[3],[1,3] -> 0+1+3+2 = 6)
  Input : [5,1,6]    Output: 28""",
{
"Python":'''
class Solution:
    def subsetXORSum(self, nums):
        total = 0
        def dfs(i, cur):
            nonlocal total
            if i == len(nums): total += cur; return
            dfs(i+1, cur)
            dfs(i+1, cur ^ nums[i])
        dfs(0, 0)
        return total

if __name__ == "__main__":
    print(Solution().subsetXORSum([1,3]), Solution().subsetXORSum([5,1,6]))
''',
"JavaScript":'''
var subsetXORSum = function(nums) {
    let total = 0;
    const dfs = (i, cur) => {
        if (i === nums.length) { total += cur; return; }
        dfs(i+1, cur); dfs(i+1, cur ^ nums[i]);
    };
    dfs(0, 0);
    return total;
};
console.log(subsetXORSum([1,3]), subsetXORSum([5,1,6]));
''',
"Java":'''
public class __CLASS__ {
    int total = 0;
    public int subsetXORSum(int[] nums) { total = 0; dfs(nums, 0, 0); return total; }
    void dfs(int[] nums, int i, int cur) {
        if (i == nums.length) { total += cur; return; }
        dfs(nums, i+1, cur); dfs(nums, i+1, cur ^ nums[i]);
    }
    public static void main(String[] args) {
        __CLASS__ s = new __CLASS__();
        System.out.println(s.subsetXORSum(new int[]{1,3}) + " " + s.subsetXORSum(new int[]{5,1,6}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
    int total;
    void dfs(vector<int>& a, int i, int cur) {
        if (i == (int)a.size()) { total += cur; return; }
        dfs(a, i+1, cur); dfs(a, i+1, cur ^ a[i]);
    }
public:
    int subsetXORSum(vector<int>& nums) { total = 0; dfs(nums, 0, 0); return total; }
};
int main() {
    Solution s;
    vector<int> a = {1,3}, b = {5,1,6};
    cout << s.subsetXORSum(a) << " " << s.subsetXORSum(b) << endl;
}
''',
"Go":'''
package main
import "fmt"
func subsetXORSum(nums []int) int {
    total := 0
    var dfs func(i, cur int)
    dfs = func(i, cur int) {
        if i == len(nums) { total += cur; return }
        dfs(i+1, cur); dfs(i+1, cur ^ nums[i])
    }
    dfs(0, 0)
    return total
}
func main() { fmt.Println(subsetXORSum([]int{1,3}), subsetXORSum([]int{5,1,6})) }
''',
"R":'''
subsetXORSum <- function(nums) {
    total <- 0
    dfs <- function(i, cur) {
        if (i > length(nums)) { total <<- total + cur; return() }
        dfs(i+1, cur); dfs(i+1, bitwXor(cur, nums[i]))
    }
    dfs(1, 0)
    total
}
print(c(subsetXORSum(c(1,3)), subsetXORSum(c(5,1,6))))
''',
}))

if __name__ == "__main__":
    write_lessons(LESSONS)
