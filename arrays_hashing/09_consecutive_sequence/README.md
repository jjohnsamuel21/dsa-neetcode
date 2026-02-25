## Longest Consecutive Sequence

### Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

### Brute Force
- Sort the array
- Iterate through the sorted array to find consecutive sequences
- Time: O(n log n) for sorting
- Space: O(1) if sorting in place

### Optimized Approach
- Remove duplicates and sort the array
- Track current consecutive count while iterating
- Update maximum when sequence breaks

### Complexity
- Time: O(n log n) due to sorting
- Space: O(n) for set and sorted list

### Key Learning
- Sorting can simplify sequence detection
- For O(n) solution, use a HashSet to check for consecutive elements without sorting