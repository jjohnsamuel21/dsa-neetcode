// SOLUTION 1

class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let l = 0;
        let r = numbers.length - 1;
        while (l < r) {
            const sum = numbers[l] + numbers[r];
            if (sum === target) {
                return [l + 1, r + 1];
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
    }
}

// SOLUTION 2
class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let hash_map = {}
        for (let i = 0; i < numbers.length; i ++) {
            const difference = target - numbers[i]
            if (difference in hash_map) {
                return [hash_map[difference], i + 1]
            }
            hash_map[numbers[i]] = i + 1
        }
    }
}
