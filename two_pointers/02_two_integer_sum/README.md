## Two Sum

### Problem
Given a **sorted** integer array `numbers` and an integer `target`, return the 1-indexed positions of two numbers such that they add up to `target`. Assume exactly one solution exists.

### Solution 1 (Two Pointers)
- Use two pointers (`l` starting at 0, `r` starting at end)
- Compute `sum = numbers[l] + numbers[r]`
  - If `sum == target`, return `[l+1, r+1]`
  - If `sum < target`, increment `l`
  - If `sum > target`, decrement `r`
- This works in O(n) time because the array is sorted

### Solution 2 (Hash Map)
- Iterate through `numbers`, storing seen values in a hash map mapping value → 1-indexed position
- For each `num`, compute `diff = target - num`
- If `diff` exists in the map, return `[map[diff], current_index]`
- This also finds a valid pair in O(n) time without requiring sorting

### Example
Input: `numbers = [2, 3, 4], target = 6`
Output: `[1, 3]`  (because `2 + 4 = 6`)

### Complexity
- Time: O(n)
- Space: O(1) for two-pointer solution (ignoring output)
- Space: O(n) for hash-map solution

### Key Learning
- For sorted inputs, two-pointer is simple and space-efficient
- Hash maps are great for unsorted inputs or when you want a single pass with O(n) space
- Maintain 1-indexed positions when required by problem conventions
