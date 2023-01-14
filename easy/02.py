# Leetcode - Desafio 217 - Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 

        confere_numero = set()#cria conjunto

        for cada_numero in nums: #para cada número da lista:
            if cada_numero in confere_numero: #se conter números repetidos:
                return True #retorne verdadeiro

            confere_numero.add(cada_numero) #método que adiciona o elemento repetido ao conjunto(set).
        return False #Se conter números distintos, retorna falso. 


# Link do Desafio Leetcode
# https://leetcode.com/problems/contains-duplicate/

#  Os sets(conjuntos) em python são utilizados ​​para armazenar vários itens em uma única variável e que gera itens não duplicados, não indexados e  imutáveis (não podem ser alterados, ms podem ser removidos ou adicionado novos itens).

# Referências
# https://realpython.com/python-sets/
# https://algoritmosempython.com.br/cursos/programacao-python/conjuntos/