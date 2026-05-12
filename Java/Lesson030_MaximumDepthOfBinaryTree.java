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

public class Lesson030_MaximumDepthOfBinaryTree {
    static class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
    public static void main(String[] args) {
        TreeNode r = new TreeNode(3); r.left = new TreeNode(9);
        r.right = new TreeNode(20); r.right.left = new TreeNode(15); r.right.right = new TreeNode(7);
        System.out.println(new Lesson030_MaximumDepthOfBinaryTree().maxDepth(r));
    }
}
