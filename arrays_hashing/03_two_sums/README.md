## Two Sum

### Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Brute Force
- Use nested loops to check every pair of numbers
- If the sum equals target, return their indices
- Time: O(n²)
- Space: O(1)

### Optimized Approach
- Use a HashMap to store numbers and their indices as we iterate
- For each number, calculate the complement (target - num)
- If complement exists in the map, return the indices
- Otherwise, store the current number and index

### Complexity
- Time: O(n)
- Space: O(n)

### Key Learning
- HashMap provides O(1) average-time complexity for lookups
- Single pass through the array is efficient for this problem