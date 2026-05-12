//go:build ignore

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

package main
import "fmt"
type TreeNode struct { Val int; Left,Right *TreeNode }
func maxDepth(root *TreeNode) int {
    if root == nil { return 0 }
    l := maxDepth(root.Left); r := maxDepth(root.Right)
    if l > r { return 1 + l }; return 1 + r
}
func main() {
    r := &TreeNode{Val:3, Left:&TreeNode{Val:9},
        Right:&TreeNode{Val:20, Left:&TreeNode{Val:15}, Right:&TreeNode{Val:7}}}
    fmt.Println(maxDepth(r))
}
