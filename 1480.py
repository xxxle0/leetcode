class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results: List[int]
        prev = 0
        for v in nums:
            results.append(prev + i)
            prev = i + prev
        return results
