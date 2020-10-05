/*

Problem Statement : (https://leetcode.com/problems/binary-search-tree-iterator/) <-- (link to the problem decription) 

*/

// Solution:

// Method - I (In order traversal)

/* time complexity : 
	
   	For constructor : O(n) 
   	For next() method : O(1)
	For hasNext() method : O(1)
*/

// Space complexity : O(n) <-- (For nodes array list)

// code:

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
class BSTIterator {
    
    private List<TreeNode> nodes;
    private int iterator;

    public BSTIterator(TreeNode root) {
        
        this.nodes = new ArrayList();
        this.iterator = 0;
        
        this.fetchNodes(root);
        
    }
    
    /** @return the next smallest number */
    public int next() {
        
        return this.nodes.get(this.iterator++).val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        
        return this.iterator < this.nodes.size();
    }
    
    private void fetchNodes(TreeNode root) {
        
        if(root == null) return;
        
        this.fetchNodes(root.left);
        this.nodes.add(root);
        this.fetchNodes(root.right);
    } 
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
