/*
Problem Statement: (https://leetcode.com/problems/count-and-say/) --> (link to the problem description)
*/

Solution: --> (Method - I):

class Solution {
public:
    string countAndSay(int n) {
        
        if(n == 1) return "1";
        
        string resultString = "1";
        
        for(int i=0; i<n-1; i++) {
            int counter = 1;
            char aCharacter = resultString[0];
            string copyString = "";
            for(int j=1; j<resultString.size(); j++) {
                if(aCharacter != resultString[j]) {
                    copyString += to_string(counter) + aCharacter;
                    counter = 1;
                    aCharacter = resultString[j];
                } else {
                    counter++;
                }
            }
            copyString += to_string(counter) + aCharacter;
            resultString = copyString;
        }
        
        return resultString;
    }
};
