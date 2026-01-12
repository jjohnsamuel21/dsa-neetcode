# SOLUTION 1
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if (len(s) != len(t)):
#             return False
#         sorted_s = "".join(sorted(s))
#         sorted_t = "".join(sorted(t))
#         for i in range(0, len(s)):
#             if (sorted_s[i] != sorted_t[i]):
#                 return False
#         return True

# value = Solution()
# result = value.isAnagram("racecar", "carrace")
# print(result)


# SOLUTION 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        hashed_values = {}
        for i in range(0, len(s)):
            if (s[i] not in hashed_values):
                hashed_values[s[i]] = 0
            hashed_values[s[i]] += 1
            if (t[i] not in hashed_values):
                hashed_values[t[i]] = 0
            hashed_values[t[i]] -= 1
        for value in hashed_values.values():
            if (value != 0):
                return False
            
        return True

value = Solution()
result = value.isAnagram("racecar", "carracr")
print(result)