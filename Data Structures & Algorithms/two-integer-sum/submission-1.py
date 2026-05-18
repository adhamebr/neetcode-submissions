class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = [-2,-2]
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] + nums[j] == target and sol ==  [-2,-2] and i!=j:
                    sol = [i,j]
        return sol


        