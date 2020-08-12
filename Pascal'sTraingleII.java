/*
Problem Statement: (https://leetcode.com/problems/pascals-triangle-ii/) <-- (link to the problem description)
*/

// Solution: Method - I (space optimised on k)

class Solution {
    public List<Integer> getRow(int k) {
        
        List<Integer> res = new ArrayList<>();
        
        int[][] cons = new int[2][k+1];
        
        cons[0][0] = 1;
        
        for(int i = 1; i < k+1; i++) {
            for(int j = 0; j < k+1; j++) {
                if(i%2 != 0) {
                    if(j == 0 || (cons[(i%2)-1][j] == 0 && j <= i)) 
                        cons[i%2][j] = 1;
                    else 
                        cons[i%2][j] = cons[(i%2)-1][j-1] + cons[(i%2)-1][j];
                } else {
                    if(j == 0 || (cons[(i%2)+1][j] == 0 && j <= i)) 
                        cons[i%2][j] = 1;
                    else 
                        cons[i%2][j] = cons[(i%2)+1][j-1] + cons[(i%2)+1][j];
                }
            }
        }
        
        for(int j = 0; j < k+1; j++) {
            res.add(cons[k%2][j]);
        }
        
        return res;
    }
}
