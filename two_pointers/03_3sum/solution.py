class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
        result = []
        dup_check = {}
        for i in range(len(nums)):
            first_val = nums[i]
            l = 0; r = len(nums) - 1
            while l < r:
                sum_value = nums[l] + nums[r]
                if sum_value + first_val == 0:
                    if i != l and l != r and i != r:
                        sortedArr = sorted([nums[i], nums[l], nums[r]])
                        stringChange = "".join(map(str, sortedArr))
                        if stringChange not in dup_check:
                            result.append(sortedArr)
                            print(i, l, r, "result append ")
                            dup_check[stringChange] = [nums[i], nums[l], nums[r]]
                    print(i, l, r, "before")
                    l += 1
                    print(i, l, r, "after")
                elif sum_value > first_val:
                    r -= 1
                elif sum_value < 0:
                    l += 1
                else:
                    break
        
        return result
    
nums = [-2,0,1,1,2]
obj = Solution().threeSum(nums)
print(obj)