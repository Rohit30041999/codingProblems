class Toeplitz {
  // A Toeplitz Matrix is a matrix in which every
  // diagonal has elements which are equal to each other
  public static boolean isToeplitz(int[][] mat) {
    int n = mat.length;
    // not a toeplitz if no elements (doubt)
    if(n == 0) return false;
    int m = mat[0].length;
    // not a toeplitz if no of rows not equal to
    // no of columns (doubt)
    if(n != m) return false;
    // m - 1 : ignore the diagonal which has only
    //         one element.
    for(int j = 0; j < m - 1; ++j) {
      int I = 0, J = j, f = mat[I][J];
      while(I < n && J < m)
        if(f != mat[I++][J++])
          return false;
    }
    // n - 1 : ignore the diagonal which has only
    //         one element.
    for(int i = 1; i < n - 1; ++i) {
      int I = i, J = 0, f = mat[I][J];
      while(I < n && J < m)
        if(f != mat[I++][J++])
          return false;
    }
    // the given matrix is a toeplitz if everything
    // is fine
    return true;
  }
  public static void main(String args[]) {
    int[][] matrix = new int[][] {
      {1, 2},
      {3, 4}
    };
    System.out.println(isToeplitz(matrix));
  } 
}
