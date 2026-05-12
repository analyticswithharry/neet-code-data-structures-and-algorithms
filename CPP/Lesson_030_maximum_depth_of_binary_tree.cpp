// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 030 -- Maximum Depth of Binary Tree
// Category   : Trees
// Difficulty : Easy
// Study Plan : Day 15
// =============================================================
//
// QUESTION:
//   Given the root of a binary tree, return its maximum depth (number of
//   nodes along the longest path from the root down to the farthest leaf).
//
//   Example:
//     Input : [3,9,20,null,null,15,7]
//     Output: 3
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
