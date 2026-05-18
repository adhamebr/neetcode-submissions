class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes_sol = {}
        sol = [-2,-2]
        for i in range(0,len(nums)):
            if nums[i] in indexes_sol:
                if i != indexes_sol[nums[i]]:
                    sol = [indexes_sol[nums[i]],i ]
                    return sol
            indexes_sol[target - nums[i]] = i

         


        