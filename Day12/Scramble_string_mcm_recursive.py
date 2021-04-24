class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if s1==s2:
            return True
        if len(s1)<=1:
            return False
        if n1==0 or n2==0:
            return False
        
        
        
        flag = False
        
        for i in range(1,min(n1,n2)):
            #print(s1,s2)
            
            if (self.isScramble(s1[0:i],s2[n2-i:n2]) and self.isScramble(s1[i:n1],s2[0:n2-i])) or (self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:n1],s2[i:n2])):
                flag = True
                break
        return flag
