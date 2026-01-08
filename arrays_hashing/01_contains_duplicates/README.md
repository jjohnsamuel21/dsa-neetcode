## Contains Duplicate

### Problem
Given an integer array `nums`, return `true` if any value appears at least twice.

### Brute Force
- Compare every pair
- Time: O(n²)
- Space: O(1)

### Optimized Approach
- Use a HashSet to track seen elements
- If an element already exists → duplicate found

### Complexity
- Time: O(n)
- Space: O(n)

### Key Learning
- HashSet is useful when fast lookup is required
