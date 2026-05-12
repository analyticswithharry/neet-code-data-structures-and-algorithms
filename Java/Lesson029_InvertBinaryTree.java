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

public class Lesson029_InvertBinaryTree {
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
        TreeNode r = new Lesson029_InvertBinaryTree().invertTree(root);
        System.out.println(r.val + " " + r.left.val + " " + r.right.val);
    }
}
