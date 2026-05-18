class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        cumm_sum=1
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        for i in nums:
            if i != 0:
                cumm_sum = cumm_sum*i

        sol_arr = len(nums)*[0]
        for i in range(0,len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    sol_arr[i] = cumm_sum
                else:
                    sol_arr[i] = 0
            else:
                sol_arr[i] = cumm_sum // nums[i]
        return sol_arr
