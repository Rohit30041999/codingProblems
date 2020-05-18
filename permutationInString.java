/*
Problem Statement: (https://leetcode.com/problems/permutation-in-string/) --> (link to the problem statement)

Solution(or Code): (Method I --> Sliding Window)
*/

class Solution {
    
    // This method is to check is the frequency of each character in both the strings are equal are or not.
    // It both are having equal number of characters and types too then it returns true.
    public static boolean isEqual(int[] c1, int[] c2) {
        
        for(int i=0; i<26; i++) if(c1[i] != c2[i]) return false;
        
        return true;
        
    }
    
    public boolean checkInclusion(String s1, String s2) {
        
        // return false length s1 is greater than s2's length.
        if(s1.length() > s2.length()) return false;
        
        // array to count the frequency of characters in s1 string.
        int[] countS1 = new int[26];
        
        // array to count the frequency of each substring's characters. Each substring will have a length of s1.
        int[] countS2 = new int[26];
        
        // Accessing the first substring from the string s2.
        String subString = s2.substring(0, 0+s1.length());
        
        for(int i=0; i<subString.length(); i++) countS2[subString.charAt(i)-'a']++;
        
        for(int i=0; i<s1.length(); i++) countS1[s1.charAt(i)-'a']++;
        
        if(isEqual(countS1, countS2)) return true;
        
        // first character of the substring.
        char firstChar = subString.charAt(0);
        
        for(int i=1; i<=s2.length()-s1.length(); i++) {
            
            char lastChar = s2.charAt(i+s1.length()-1);
            
            // removing the first character's frequency. Means removing the character from the substring.
            countS2[firstChar-'a']--;
            
            firstChar = s2.charAt(i);
            
            // adding the last(next) character's frequency. Means appending a new character to the substring after removing the first.
            countS2[lastChar-'a']++;
            
            if(isEqual(countS1, countS2)) return true;
        
        }
        
        // returning false if there is no permutation in the string s2.
        return false;
    }
}
