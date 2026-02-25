## Group Anagrams

### Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Brute Force
- For each string, compare with every other string to check if they are anagrams
- Use sorting or character counting for comparison
- Time: O(n² * m log m) where n is number of strings, m is max string length
- Space: O(n * m)

### Optimized Approach
- Sort each string to create a key
- Use a HashMap with sorted string as key and list of original strings as value
- Group strings that have the same sorted key

### Complexity
- Time: O(n * m log m) for sorting all strings
- Space: O(n * m) for storing the groups

### Key Learning
- Sorting strings creates a consistent key for anagrams
- HashMap is efficient for grouping operations