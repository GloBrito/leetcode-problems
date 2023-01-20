# Leetcode - Desafio 53 - Máximo Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maior_soma = nums[0] 
        soma = 0

        for cada_valor in nums:
            soma += cada_valor
    
            if soma > maior_soma:
                maior_soma = soma
    
            if soma < 0:
                soma = 0

        return maior_soma

# Link do Desafio Leetcode
# https://leetcode.com/problems/maximum-subarray/description/
















# https://leetcode.com/problems/maximum-subarray/