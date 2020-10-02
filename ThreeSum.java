/*

Problem Statement: (https://leetcode.com/problems/3sum/) <--- (link to the problem description)


Solution: Method - 1 (Sorting + Two Pointer)

*/

class Solution {
    
    List<List<Integer>> combinations;
    
    public List<List<Integer>> threeSum(int[] nums) {
        
        combinations = new ArrayList<>();
        
        Arrays.sort(nums);
        
        for(int idx = 0; idx < nums.length - 2; idx++) {
            
            int currentNumber = nums[idx];
            
            if(idx > 0 && currentNumber == nums[idx - 1]) continue;
            
            int start = idx + 1, end = nums.length - 1;
            
            while(start < end) {
                
                int number2 = nums[start], number3 = nums[end];
                
                if(currentNumber + number2 + number3 > 0) {
                    
                    end--;
                    
                } else if(currentNumber + number2 + number3 < 0) {
                    
                    start++;
                    
                } else {
                    
                    Integer[] array = {currentNumber, number2, number3};
                    
                    combinations.add(Arrays.asList(array));
                    
                    start++;
                    
                    while(nums[start] == nums[start-1] && start < end) start++;
                }
            }
        }
        
        return combinations;
    }
}
