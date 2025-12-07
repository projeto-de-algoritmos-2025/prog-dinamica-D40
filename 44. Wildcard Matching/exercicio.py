class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_ptr, p_ptr = 0, 0
        last_s_star, last_p_star = -1, -1
        
        while s_ptr < len(s):
            # 1. Caracteres coincidem ou padrão tem '?'
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            
            # 2. Padrão tem '*': registramos a posição para possível retorno (backtrack)
            elif p_ptr < len(p) and p[p_ptr] == '*':
                last_p_star = p_ptr
                last_s_star = s_ptr
                p_ptr += 1
            
            # 3. Não coincide, mas houve um '*' anteriormente: tentamos o próximo caractere de 's'
            elif last_p_star != -1:
                p_ptr = last_p_star + 1
                last_s_star += 1
                s_ptr = last_s_star
            
            # 4. Não coincide e não há '*' para salvar: falha
            else:
                return False
        
        # Verificar se restam apenas '*' no padrão p
        return all(x == '*' for x in p[p_ptr:])
