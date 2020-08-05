/*
Problem Description : 

	Design a data structure that supports the following two operations:

		i) void addWord(word)
		ii) bool search(word)
	
	search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

	Example:

		addWord("bad")
		addWord("dad")
		addWord("mad")
		search("pad") -> false
		search("bad") -> true
		search(".ad") -> true
		search("b..") -> true
	Note:
		You may assume that all words are consist of lowercase letters a-z.
*/


// Solution : Method - I (Using Trie but it's a slow algorithm)

// Trie Data structure to store the words.
class Trie {
    
    boolean isEnd; // isEnd is a boolean variable used to show wheather this is the end of the word or not.
    Trie[] t; 
    
    public Trie() {
        
        t = new Trie[26]; // size 26 for 26 lower case characters.
        
        for(int i = 0; i < 26; i++) 
            t[i] = null;
    }
}


class WordDictionary {
    
    Trie trie;
    /** Initialize your data structure here. */
    public WordDictionary() {
        trie = new Trie();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        
        Trie current = trie;
        
        for(int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            
            if(current.t[c - 'a'] == null) {
                current.t[c - 'a'] = new Trie();
            }
            
            current = current.t[c - 'a'];
        }
        
        current.isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        
        char[] letters = word.toCharArray();
        
        return isThere(letters, 0, letters.length, trie);
    }
    
    public static boolean isThere(char[] l, int i, int n, Trie trie) {
        
        if(i >= n) return trie.isEnd;
        
        if(l[i] != '.') {
            if(trie.t[l[i] - 'a'] != null) {
                return isThere(l, i+1, n, trie.t[l[i] - 'a']);
            }
            return false;
        }
        
        if(l[i] == '.') {
            for(int j = 0; j < 26; j++) {
                if(trie.t[j] != null) {
                    if(isThere(l, i+1, n, trie.t[j])) 
                        return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
