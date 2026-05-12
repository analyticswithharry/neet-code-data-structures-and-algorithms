//go:build ignore

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

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    cur := root
    for cur != nil {
        if p.Val < cur.Val && q.Val < cur.Val { cur = cur.Left
        } else if p.Val > cur.Val && q.Val > cur.Val { cur = cur.Right
        } else { return cur }
    }
    return nil
}
func main() {
    p := &TreeNode{Val:2}; q := &TreeNode{Val:8}
    r := &TreeNode{Val:6, Left:p, Right:q}
    fmt.Println(lowestCommonAncestor(r,p,q).Val)
}
