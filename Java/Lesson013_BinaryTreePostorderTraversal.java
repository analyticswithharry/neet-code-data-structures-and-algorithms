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

import java.util.*;
public class Lesson013_BinaryTreePostorderTraversal {
    static class TreeNode { int val; TreeNode left, right; TreeNode(int v){val=v;} }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>(); Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root, last = null;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            TreeNode peek = st.peek();
            if (peek.right != null && last != peek.right) cur = peek.right;
            else { out.add(peek.val); last = st.pop(); }
        }
        return out;
    }
    public static void main(String[] args) {
        TreeNode r = new TreeNode(1); r.right = new TreeNode(2); r.right.left = new TreeNode(3);
        System.out.println(new Lesson013_BinaryTreePostorderTraversal().postorderTraversal(r));
    }
}
