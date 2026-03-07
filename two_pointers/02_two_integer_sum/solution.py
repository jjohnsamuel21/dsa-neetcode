# Solution 1

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0; r = len(numbers) - 1
        while l < r:
            sum_value = numbers[l] + numbers[r] 
            if sum_value > target:
                r -= 1
            elif sum_value < target:
                l += 1
            else:
                return [l + 1, r + 1]



# Solution 2
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i+1, ]
            hash_map[num] = i+1

numbers = [2, 3, 4]
target = 6
result = Solution().twoSum(numbers, target)
print(result)