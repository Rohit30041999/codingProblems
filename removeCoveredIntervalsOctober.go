/*

problem statement : (leetcode October Challenge 2020)

	Given a list of intervals, remove all intervals that are covered by another interval in the list.

	Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

	After doing so, return the number of remaining intervals.

 

	Example 1:

		Input: intervals = [[1,4],[3,6],[2,8]]
		Output: 2

		Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

	Example 2:

		Input: intervals = [[1,4],[2,3]]
		Output: 1

	Example 3:

		Input: intervals = [[0,10],[5,12]]
		Output: 2

	Example 4:

		Input: intervals = [[3,10],[4,10],[5,11]]
		Output: 2

	Example 5:

		Input: intervals = [[1,2],[1,4],[3,4]]
		Output: 1
 

	Constraints:

		1) 1 <= intervals.length <= 1000
		2) intervals[i].length == 2
		3) 0 <= intervals[i][0] < intervals[i][1] <= 10^5
		4) All the intervals are unique.
		
*/

// Solution : Method - 1 (Two nested loops with a boolean array for covered intervals)

func removeCoveredIntervals(intervals [][]int) int {
    
    var sizeOfArr int = len(intervals)
    var coveredIntervals = make([]bool, sizeOfArr)
    var totalNumberOfIntervals int
    
    for i_idx := 0; i_idx < len(intervals); i_idx++ {
        if coveredIntervals[i_idx] == false {
            currentInterval := intervals[i_idx]
            c := currentInterval[0]
            d := currentInterval[1]
            for j_idx := 0; j_idx < len(intervals); j_idx++ {
                if i_idx != j_idx {
                    anotherInterval := intervals[j_idx]
                    a := anotherInterval[0]
                    b := anotherInterval[1]
                    if c <= a && b <= d { coveredIntervals[j_idx] = true }                    
                }
            }
        }
    }
    
    for i_idx := 0; i_idx < len(intervals); i_idx++ { 
        if coveredIntervals[i_idx] == false { totalNumberOfIntervals++ } 
    }
    
    return totalNumberOfIntervals
    
}
