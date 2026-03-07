## Valid Palindrome

### Problem
Given a string `s`, return `true` if it is a palindrome after removing all non-alphanumeric characters and ignoring case.

### Approach
- Normalize the string:
  - Remove non-alphanumeric characters
  - Convert to lowercase
- Use two pointers (start + end) to compare characters while moving inward
- If any pair mismatches, return `false`. Otherwise return `true` once pointers cross

### Complexity
- Time: O(n) (where n is the length of the string)
- Space: O(n) (for the filtered/normalized string)

### Key Learning
- Two-pointer approach is efficient for palindrome checks
- Preprocessing input (filter + normalize) simplifies logic for edge cases
