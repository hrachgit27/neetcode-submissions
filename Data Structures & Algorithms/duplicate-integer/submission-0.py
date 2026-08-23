class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        Listset = set()
        for num in nums:
            if num in Listset:
                return True
            Listset.add(num)

        
        return False