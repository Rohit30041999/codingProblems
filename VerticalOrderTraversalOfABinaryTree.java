/*
Problem Statement: (https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) <-- (link to the problem description)
*/

// Solution: Method - I (TreeMap and PriorityQueue(min heap) of pairs({y, val_of_node}))


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

// helper comparator: >>>>
class Val_Comp implements Comparator<ArrayList<Integer>> {
    
    public int compare(ArrayList<Integer> pair1, ArrayList<Integer> pair2) {
        
        int f1 = pair1.get(0), f2 = pair2.get(0);
        int s1 = pair1.get(1), s2 = pair2.get(1);
        
        if(f1 != f2) 
            return f1 - f2;
        
        return s1 - s2;
    }
}

class Solution {
    
    static Map<Integer, PriorityQueue<ArrayList<Integer>>> map;
    
	// main function: >>>>
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        
        map = new TreeMap<>();
        List<List<Integer>> traversedValues = new ArrayList<>();
        
        traverse(root, 0, 0);
        
        for(PriorityQueue<ArrayList<Integer>> set: map.values()) {
            
            PriorityQueue<ArrayList<Integer>> cur = set;
            ArrayList<Integer> nodeValues = new ArrayList<>();
            
            while(!cur.isEmpty()) {
                
                ArrayList<Integer> pair = cur.poll();
                
                nodeValues.add(pair.get(1));
            }
            
            traversedValues.add(nodeValues);
        }
        
        return traversedValues;
    }
    
	// helper function: >>>>
    public static void traverse(TreeNode root, int x, int y) {
        
        if(root == null) return;
        
        traverse(root.left, x-1, y+1);
        
        if(map.containsKey(x)) {
            
            PriorityQueue<ArrayList<Integer>> minHeap = map.get(x);
            ArrayList<Integer> pair = new ArrayList<>();
            
            pair.add(y);
            pair.add(root.val);
            
            minHeap.add(pair);
            
            map.put(x, minHeap);
            
        } else {
            
            PriorityQueue<ArrayList<Integer>> minHeap = new PriorityQueue<>(new Val_Comp());
            ArrayList<Integer> pair = new ArrayList<>();
            
            pair.add(y);
            pair.add(root.val);
            
            minHeap.add(pair);
            
            map.put(x, minHeap);
            
        }
        
        traverse(root.right, x+1, y+1);
    }
}
