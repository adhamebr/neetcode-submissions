class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [1] * (n+2)
        suff = [1] * (n+2)

        pref_cum_sum=1
        for i in range(0,len(nums)):
            pref_cum_sum = pref_cum_sum * nums[i]
            pref[i+1] = pref_cum_sum
    
        suf_cum_sum=1    
        i = 0
        for j in range(len(nums)-1,-1,-1):
            suf_cum_sum = suf_cum_sum * nums[j]
            suff[i+1] = suf_cum_sum
            i+=1

        sol = n*[1]
        n=n-1
        for i in range(0,n+1):

            sol[i] = suff[n-i] * pref[i]

        return sol