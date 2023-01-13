class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

    
palavra = "hello"
vogais_da_palavra = []
vogais = ["a", "e", "i", "o", "u"]

for letra in palavra : #para cada letra da palvra, faça:
    if letra in vogais: #se letra é uma vogal:
        vogais_da_palavra.append(letra)


print(vogais_da_palavra)





# https://leetcode.com/problems/reverse-vowels-of-a-string/