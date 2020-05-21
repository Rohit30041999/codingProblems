/*
Problem Statement: (https://leetcode.com/problems/count-square-submatrices-with-all-ones/) --> (link to the problem description)

Solution: (Method - I --> (Dynamic Programming(Bottom Up)))
*/

class Solution {
    public int countSquares(int[][] A) {
        
        int count = 0;
        
        for(int i = 1; i < A.length; i++) {
            for(int j = 1; j < A[i].length; j++) {
                if(A[i][j] == 1) {
                    A[i][j] = A[i][j] + Math.min(A[i-1][j-1], Math.min(A[i-1][j], A[i][j-1]));
                }
            }
        }
        
        for(int i = 0; i < A.length; i++) {
            for(int j = 0; j < A[i].length; j++) {
                count += A[i][j];
            }
        }
        
        return count;
        
    }
}
