/*
Problem Statement: (https://leetcode.com/problems/string-compression/) --> (link to the problem description)
*/

Solution:--> (Method - I):

class Solution {
public:
    int compress(vector<char>& chars) {
        char c = chars[0];
        int counter = 1;
        vector<char> res;
        for(int i=1; i<chars.size(); i++) {
            if(c != chars[i]) {
                res.push_back(c);
                vector<char> s;
                if(counter != 1) {
                    while(counter > 0) {
                        int rem = counter%10;
                        s.push_back((char)(rem+48));
                        counter /= 10;
                    }
                    for(int i=s.size()-1; i>=0; --i) {
                        res.push_back(s[i]);
                    }
                }
                counter = 1;
                c = chars[i];
            } else {
                counter++;
            }
        }
        
        res.push_back(c);
        vector<char> s;
        if(counter != 1) {
            while(counter > 0) {
                int rem = counter%10;
                s.push_back((char)(rem+48));
                counter /= 10;
            }

            for(int i=s.size()-1; i>=0; --i) {
                res.push_back(s[i]);
            }
        }
        
        chars.clear();
        for(int i=0; i<res.size(); i++) {
            chars.push_back(res[i]);
        }
        
        return chars.size();
    }
};
