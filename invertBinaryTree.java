// (Source --> LeetCode)

// Solution: (Method - I : Recursion)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        
        // if null return that null root.
        if(root == null) return root;
        
        // store back the right sub tree or node.
        root.right = invertTree(root.right);
        
        // store back the left sub tree or node.
        root.left = invertTree(root.left);
        
        // Swap the nodes.
        TreeNode tempNode = root.right;
        root.right = root.left;
        root.left = tempNode;
        
        // return the main root node.
        return root;
    }
}
