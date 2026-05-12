// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 013 -- Binary Tree Postorder Traversal
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 7
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return the postorder
//   (Left, Right, Root) traversal of its nodes' values.
//
//   Example:
//     Input : root = [1,null,2,3]
//     Output: [3, 2, 1]
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
