// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 024 -- Word Search II
// Category   : Tries
// Difficulty : Hard
// Study Plan : Day 12
// =============================================================
//
// QUESTION:
//   Given an m x n board of characters and a list of strings words, return
//   all words on the board. Each word must be constructed from letters of
//   sequentially adjacent cells (horizontal/vertical). The same cell may not
//   be used more than once in a word.
//
//   Example:
//     board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
//     words=["oath","pea","eat","rain"]
//     Output: ["oath","eat"]
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
