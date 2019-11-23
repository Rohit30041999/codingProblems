/*
Maximum length of a square of 1's in a matrix (Dynamic Programming):>>
example :
matrix :       1 1 0 0 1
               1 1 1 1 0
               0 1 1 1 1
               1 1 1 1 1
    if you can observe. The max square is ==>    1 1 1
                                                 1 1 1
                                                 1 1 1
    so return length of its side i.e., 3.
*/

import java.io.*;
import java.util.*;
import java.lang.*;
class MaxSquare {
  private static int maxSquareOnes(int[][] matrix) {
    int lengthOfSq = Integer.MIN_VALUE;
    int[][] clone = matrix.clone();
    for(int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[0].length; j++) {
        if (i > 0 && j > 0) {
          int minPrev = Math.min(matrix[i][j - 1], Math.min(matrix[i - 1][j], matrix[i - 1][j - 1]));
          clone[i][j] = clone[i][j] + minPrev;
          if (lengthOfSq < clone[i][j]) {
            lengthOfSq = clone[i][j];
          }
        }
      }
    }
    return lengthOfSq;
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    int[][] matrix = new int[n][m];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = sc.nextInt();
      }
    }
    int maxSquareLength = maxSquareOnes(matrix);
    System.out.println(maxSquareLength);
    sc.close();
  }
}
