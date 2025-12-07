class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        resultado = []
        
        def backtrack(string_atual, abertos, fechados):
            
            if len(string_atual) == 2 * n:
                resultado.append(string_atual)
                return
            
            
            if abertos < n:
                backtrack(string_atual + "(", abertos + 1, fechados)
                
            
            if fechados < abertos:
                backtrack(string_atual + ")", abertos, fechados + 1)
        
        # Início da recursão
        backtrack("", 0, 0)
        return resultado
