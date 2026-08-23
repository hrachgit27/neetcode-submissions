class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = []

        for index, num in enumerate(nums):
            for index2, num in enumerate(nums):
                if index != index2 and nums[index] + nums[index2] == target:
                    numbers.append(index)
                    numbers.append(index2)
                    return numbers


        return numbers

