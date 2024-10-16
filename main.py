from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    answer = {}
    
    for i, num in enumerate(nums):
        val = target - num
        if val in answer:
            return [answer[val], i]
        answer[num] = i


