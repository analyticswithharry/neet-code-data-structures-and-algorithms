//go:build ignore

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

package main
import "fmt"
type TreeNode struct { Val int; Left, Right *TreeNode }
func postorderTraversal(root *TreeNode) []int {
    out := []int{}; st := []*TreeNode{}
    var cur, last *TreeNode = root, nil
    for cur != nil || len(st) > 0 {
        for cur != nil { st = append(st, cur); cur = cur.Left }
        peek := st[len(st)-1]
        if peek.Right != nil && last != peek.Right { cur = peek.Right
        } else { out = append(out, peek.Val); last = peek; st = st[:len(st)-1] }
    }
    return out
}
func main() {
    r := &TreeNode{Val:1, Right:&TreeNode{Val:2, Left:&TreeNode{Val:3}}}
    fmt.Println(postorderTraversal(r))
}
