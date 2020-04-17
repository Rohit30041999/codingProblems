/*
Problem Statement: (https://leetcode.com/problems/insert-interval/) --> (link to the problem description)
*/

Solution: --> (Method - I):

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& I, vector<int>& n) {
	
        bool stopMerge = false;
        vector<vector<int>> res;
		
        for(int i=0; i<I.size(); i++) {
            if(n[1] < I[i][0] && !stopMerge) {
                stopMerge = true;
                res.push_back(n);
                res.push_back(I[i]);
            } else if(n[0] <= I[i][1] && !stopMerge) {
                if(n[0] <= I[i][0] && n[1] <= I[i][1]) {
                    n[1] = I[i][1];
                } else if(n[0] > I[i][0] && n[1] <= I[i][1]) {
                    n[0] = I[i][0];
                    n[1] = I[i][1];
                } else if(n[0] > I[i][0] && n[1] > I[i][1]) {
                    n[0] = I[i][0];
                }
            } else {
                res.push_back(I[i]);
            }
        }
        
        if(!stopMerge) {
            res.push_back(n);
        }
        
        return res;
    }
};
