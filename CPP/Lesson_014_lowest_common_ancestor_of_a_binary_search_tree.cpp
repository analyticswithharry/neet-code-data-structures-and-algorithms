// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 014 -- Lowest Common Ancestor of a Binary Search Tree
// Category   : Trees
// Difficulty : Medium
// Study Plan : Day 7
// =============================================================
//
// QUESTION:
//   Given a binary search tree (BST), find the lowest common ancestor (LCA)
//   of two given nodes p and q. Both p and q exist in the BST.
//
//   Example:
//     Input : root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8
//     Output: 6
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
