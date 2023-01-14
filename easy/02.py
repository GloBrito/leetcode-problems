class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        nums = [1,1,1,3,3,4,3,2,4,2]
        confere_numero = set()

        for cada_numero in nums:
            if cada_numero in confere_numero:
                return True

            confere_numero.add(cada_numero)
        return False

        print(cada_numero)
