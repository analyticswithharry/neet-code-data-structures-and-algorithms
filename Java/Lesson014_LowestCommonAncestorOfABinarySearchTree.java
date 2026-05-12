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

public class Lesson014_LowestCommonAncestorOfABinarySearchTree {
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
        System.out.println(new Lesson014_LowestCommonAncestorOfABinarySearchTree().lowestCommonAncestor(r, p, q).val);
    }
}
