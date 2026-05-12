// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 011 -- Implement Trie Prefix Tree
// Category   : Tries
// Difficulty : Medium
// Study Plan : Day 6
// =============================================================
//
// QUESTION:
//   Implement the Trie class with:
//     insert(word)        - inserts the word
//     search(word)        - returns true if word is in trie
//     startsWith(prefix)  - returns true if any word starts with prefix
//
//   Example:
//     trie = Trie()
//     trie.insert("apple")
//     trie.search("apple")   -> True
//     trie.search("app")     -> False
//     trie.startsWith("app") -> True
//     trie.insert("app")
//     trie.search("app")     -> True
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
