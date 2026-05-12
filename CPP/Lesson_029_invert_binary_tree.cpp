// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 029 -- Invert Binary Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 15
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, invert the tree (mirror it), and
//   return its root.
//
//   Example:
//     Input : [4,2,7,1,3,6,9]
//     Output: [4,7,2,9,6,3,1]
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
