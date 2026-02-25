## Top K Frequent Elements

### Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Brute Force
- Count frequency of each element using a map
- Sort the elements by frequency in descending order
- Return the first k elements
- Time: O(n + n log n) for counting and sorting
- Space: O(n)

### Optimized Approach
- Use a HashMap to count the frequency of each element
- Sort the map entries by frequency in descending order
- Extract the top k elements

### Complexity
- Time: O(n log n) due to sorting
- Space: O(n) for the frequency map

### Key Learning
- HashMap is efficient for frequency counting
- Sorting can be used when k is not too large, but heap-based solutions exist for better performance