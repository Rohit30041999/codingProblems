/*
Problem Statement: (https://leetcode.com/problems/rotting-oranges/) <-- (link to the problem description)
*/

// Solution: Method - I (BFS approach)

class Solution {
    public int orangesRotting(int[][] g) {
        
        Queue<String> queue = new LinkedList<>();
        int times = 0;
        
        for(int i = 0; i < g.length; i++) {
            for(int j = 0; j < g[i].length; j++) {
                if(g[i][j] == 2) {
                    String compressedForm = String.valueOf(i) + " " + String.valueOf(j);
                    queue.add(compressedForm);
                }
            }
        }
        
        queue.add("");
        
        int[] di = {-1, 0, 0, 1};
        int[] dj = {0, -1, 1, 0};
        
        while(queue.size() > 1) {
            
            String cur = queue.poll();
            
            if(cur.equals("")) {
                times++;
                queue.add(cur);
            } else {
                
                String[] indexes = cur.split(" ");
                int x = Integer.parseInt(indexes[0]);
                int y = Integer.parseInt(indexes[1]);
                
                for(int i = 0; i < 4; i++) {
                    
                    int indexI = x - di[i];
                    int indexJ = y - dj[i];
                    
                    if((indexI >= 0 && indexJ >= 0) && (indexI < g.length && indexJ < g[0].length)) {
                        if(g[indexI][indexJ] == 1) {
                            g[indexI][indexJ] = 2;
                            String compressedForm = String.valueOf(indexI) + " " + String.valueOf(indexJ);
                            queue.add(compressedForm);
                        }
                    }
                }
            }
        }
        
        for(int i = 0; i < g.length; i++) {
            for(int j = 0; j < g[i].length; j++) {
                if(g[i][j] == 1) 
                    return -1;
            }
        }
        return times;
    }
}
