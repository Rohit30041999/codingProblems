/*
Problem Statement:>>> (https://practice.geeksforgeeks.org/problems/level-order-traversal/1/) -> (link to the problem description)
*/

/*
Solution:>>>

Method - I: -> (level order traversal using Queue)
*/

/*
Main Methods used in Queue Interface from Collections in JAVA:>>

QueueObject.add(element);  // add() method to add an element into the queue.
QueueObject.poll();        // poll() method to remove the first element from queue and returns it.
QueueObject.isEmpty();     // isEmpty() method to check wheather the queue is empty or not. It basically returns true or false.
QueueObject.size();        // size() method to get total number of elements present in the queue.
QueueObject.get(index);    // get() method to get the element present at that index.
QueueObject.element();     // element() method to get the first element rather than removing it.

Declaration of Queue Interface in JAVA:>>>

(1) Queue<DataType> queue = new LinkedList<>();
(2) Queue<DataType> minheap = new priorityQueue<>();
(3) Queue<DataType> maxheap = new priorityQueue<>((a, b) -> a - b);
*/

class Level_order_traversal
{
    static void levelOrder(Node node) 
    {
        if(node == null) return;
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(node);
        while(!queue.isEmpty()) {
            Node currentNode = queue.poll();
            System.out.print(currentNode.data + " ");
            if(currentNode.left != null) queue.add(currentNode.left);
            if(currentNode.right != null) queue.add(currentNode.right);
        }
    }
}
