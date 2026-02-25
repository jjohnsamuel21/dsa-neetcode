## Product of Array Except Self

### Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### Brute Force
- For each element, iterate through the array and multiply all other elements
- Time: O(n²)
- Space: O(1) excluding output

### Optimized Approach
- Compute prefix products (product of elements before i)
- Compute suffix products (product of elements after i)
- For each i, multiply prefix[i] * suffix[i]

### Complexity
- Time: O(n)
- Space: O(n) for prefix and suffix arrays

### Key Learning
- Prefix and suffix arrays can solve problems requiring products of subarrays
- Avoids division and handles zeros correctly