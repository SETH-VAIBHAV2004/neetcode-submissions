class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        for a in nums:
            prod = int(math.prod(nums[:nums.index(a)] + nums[nums.index(a) + 1:]))
            L.append(prod)
        return L