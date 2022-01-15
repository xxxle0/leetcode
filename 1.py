class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, el in enumrate(nums):
            remain = target - el
            if remain in dict:
                return [i, dict[remain]]
            dict[remain] = i
