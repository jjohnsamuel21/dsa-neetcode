## Valid Anagrams

### Problem
Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

### Solution 1
- If the length of both strings mismatch return false
- Sort both the strings
- Loop through the length of the string
- If both position character mismatches, return false

### Solution 1 - Complexity Analysis
- Time: O(n log n)
- Space: O(n)

### Solution 2
- Use a HashSet to track both string characters
- Add a positive counter(+1) for the first string and negative counter(-1) for the second string
- Loop the values of the hashset
- If any of the value is not equal to 0, return false
- Else return true

### Solution 2 - Complexity Analysis
- Time: O(n)
- Space: O(n)
