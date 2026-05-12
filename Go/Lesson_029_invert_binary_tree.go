//go:build ignore

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

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func invertTree(root *TreeNode) *TreeNode {
    if root == nil { return nil }
    l := invertTree(root.Right); r := invertTree(root.Left)
    root.Left = l; root.Right = r
    return root
}
func main() {
    r := &TreeNode{Val:4,
        Left: &TreeNode{Val:2, Left:&TreeNode{Val:1}, Right:&TreeNode{Val:3}},
        Right:&TreeNode{Val:7, Left:&TreeNode{Val:6}, Right:&TreeNode{Val:9}}}
    inv := invertTree(r)
    fmt.Println(inv.Val, inv.Left.Val, inv.Right.Val)
}
