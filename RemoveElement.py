class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for _ in range(len(nums)):
            if val in nums:
                nums.remove(val)
        print(nums)
Solution().removeElement([3,2,2,3], 3)
