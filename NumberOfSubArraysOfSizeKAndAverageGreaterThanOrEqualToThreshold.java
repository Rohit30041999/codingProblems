/*
problem description: (https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) <-- (link to the problem description)
*/

// Method - 1 (Prefix Sum):

// Code:
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
	
        // initialise a prefix sum array.
        int[] prefixSum = new int[arr.length];
        prefixSum[0] = arr[0];
        
        // perform the prefix (or cumulative) sum on the array values.
        for(int index = 1; index < arr.length; index++) {
            prefixSum[index] = arr[index] + prefixSum[index-1];
        }
        
        int res = 0; // answer : number of sub arrays.
        
        // use the prefix sum to get the averages.
        for(int i = k-1; i < arr.length; i++) {
            int backIndex = i - k;
            if(backIndex > -1) {
                int average = (prefixSum[i] - prefixSum[backIndex]) / k;
                if(average >= threshold) res++;
            } else {
                int average = prefixSum[i] / k;
                if(average >= threshold) res++;
            }
        }
        
        return res;
    }
}
