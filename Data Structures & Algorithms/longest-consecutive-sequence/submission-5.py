class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        length = 1
        maxlength = 1
        L = list(set(nums))
        L.sort()
        for a in range(len(L) - 1):
            if L[a+1] - L[a] == 1:
                length += 1
            else:
                length = 1
            maxlength = max(maxlength, length)
        return maxlength 
