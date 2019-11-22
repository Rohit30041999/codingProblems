"""
Title: WordOrder (Hacker Rank).
You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1 <= n <= pow(10, 6)
The sum of the lengths of all the words do not exceed pow(10, 6). 
All the words are composed of lowercase English letters only.

Input Format:

The first line contains the integer, .
The next  lines each contain a word.

Output Format:

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input:

4
bcdef
abcdefg
bcde
bcdef

Sample Output:

3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""

#Solution:>>

import collections

def wordOrder(words: list) -> None:
    wordDic = collections.OrderedDict()
    for word in words:
        if wordDic.get(word) is not None:
            wordDic[word] = wordDic.get(word) + 1
        else: wordDic[word] = 1
    print(len(wordDic))
    for values in list(wordDic.values()):
        print(values, end = " ")

def main():
    n = int(input().strip())
    words = []
    for i in range(n):
        word = input().strip()
        words.append(word)
    wordOrder(words)

main()
