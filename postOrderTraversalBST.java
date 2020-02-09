/*
Problem Statement:>>> () -> (link to the problem description)
*/

/*
Solution:>>>

Method - I: -> (post order traversal using stack)
*/

class Tree
{
    void postOrder(Node root)
    {
       if(root == null) return;
       List<Integer> store = new ArrayList<>();
       Stack<Node> stack = new Stack<Node>();
       stack.push(root);
       while(!stack.isEmpty()) {
           Node currentNode = stack.pop();
           store.add(currentNode.data);
           if (currentNode.left != null) stack.add(currentNode.left);
           if (currentNode.right != null) stack.add(currentNode.right);
       }
       for(int i=store.size()-1; i>=0; --i) 
	       System.out.print(store.get(i) + " ");
    }
}
