/*
Problem Statement:>>> (https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1) -> (link to the problem description)
*/

/*
Solution:>>>

Method - I: --> (level order traversal)
*/

class GfG
{
    int countLeaves(Node node) 
    {
         if(node == null) return 0;
         int countLeaves = 0;
         Queue<Node> queue = new LinkedList<Node>();
         queue.add(node);
         while(!queue.isEmpty()) {
             Node currentNode = queue.poll();
             if(currentNode.left != null) queue.add(currentNode.left);
             if(currentNode.right != null) queue.add(currentNode.right);
             else countLeaves++;
         }
         return countLeaves;
    }
}
