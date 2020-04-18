/*
Problem Statement:

	Given a number in Roman numeral format, convert it to decimal.

	The values of Roman numerals are as follows:

	{
    	'M': 1000,
    	'D': 500,
    	'C': 100,
    	'L': 50,
    	'X': 10,
    	'V': 5,
    	'I': 1
	}
	In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

	For the input XIV, for instance, you should return 14.

*/

Solution: --> (Method-I)

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
  map<char, int> hashMap;
  char a[7] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
  int initialValue = 5000;

  for(int i=0; i<sizeof(a); i++) {
    initialValue = (i%2 == 0) ? initialValue/5: initialValue/2;
    hashMap[a[i]] = initialValue;
  }
  
  string s = "XL";
  
  if(s.size() == 0) {
    cout << 0 << endl;
  } else if(s.size() == 1) {
    cout << hashMap[s[0]] << endl;
  } else {
    int n = s.size();
    int res = hashMap[s[n-1]];
    
    for(int i=(n-2); i>=0; i--) {
      if(res > hashMap[s[i]]) {
        res = res - hashMap[s[i]];
      } else {
        res = res + hashMap[s[i]];
      }
    }

    cout << res << endl;
  }
  
  return 0;
}
