// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 012 -- Design Add And Search Words Data Structure
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Design a data structure that supports:
//     addWord(word)
//     search(word)  - word may contain '.' which matches any single letter
//
//   Example:
//     d = WordDictionary(); d.addWord("bad"); d.addWord("dad"); d.addWord("mad")
//     d.search("pad") -> False
//     d.search("bad") -> True
//     d.search(".ad") -> True
//     d.search("b..") -> True
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
