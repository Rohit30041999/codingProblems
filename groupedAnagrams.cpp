/*
  (LeetCode :- groupedAnagrams).
*/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

class Solution {
  public:
    vector<int> groupedAnagrams(vector<string>& v) {

      vector<int> res;
      vector<string> subRes;
      vector<pair<string, int>> dupArr;

      for(int i=0; i<v.size(); i++) {
        string s = v[i];
        sort(s.begin(), s.end());
        dupArr.push_back({s, i});
      }

      sort(dupArr.begin(), dupArr.end());
      
      subRes.push_back(v[dupArr[0].second]);
      string start = dupArr[0].first;
      
      for(int i=1; i<dupArr.size(); i++) {
        if(start != dupArr[i].first) {
          start = dupArr[i].first;
          res.push_back(subRes.size());
          subRes.clear();
          subRes.push_back(v[dupArr[i].second]);
        } else {
          subRes.push_back(v[dupArr[i].second]);
        }
      }
      
      res.push_back(subRes.size());
      
      return res;
    }
};

int main() {
  vector<string> v = {"cat", "ate", "gold", "logd", "god"};
  Solution solution;
  vector<int> res = solution.groupedAnagrams(v);
  cout << "[";
  for(int i=0; i<res.size(); i++) {
    if(i == res.size()-1) {
      cout << res[i];
      break;
    }
    cout << res[i] << ", ";
  } cout << "]" << endl;
}
