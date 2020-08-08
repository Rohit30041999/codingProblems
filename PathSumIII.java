/*
Problem Statement: (https://leetcode.com/problems/path-sum-iii/) <-- (link to the problem description)
*/

// Solution : Method - I (Fixed each node and check for the paths whose sum is equal to sum)

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

    int res = 0;
    
    public int pathSum(TreeNode root, int sum) {
        
        checkPathsI(root, sum);
        
        return res;
    }
    
    public void checkPathsI(TreeNode root, int sum) {
        
        if(root == null) return;
        
        checkPathsII(root, sum, 0);
        
        checkPathsI(root.left, sum);
        checkPathsI(root.right, sum);
    }
    
    public void checkPathsII(TreeNode root, int sum, int curSum) {
        
        if(root == null) return;
        
        if(curSum + root.val == sum) res++;
        
        checkPathsII(root.left, sum, curSum + root.val);
        checkPathsII(root.right, sum, curSum + root.val);
    }
}
