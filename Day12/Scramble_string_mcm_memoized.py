class Solution:
    
    def isScramble(self, s1: str, s2: str) -> bool:
        dic = {}
        def isScramble1(s1: str, s2: str):
        
            key = s1 + " " + s2
            if key in dic:
                return dic[key]

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

                if (isScramble1(s1[0:i],s2[n2-i:n2]) and isScramble1(s1[i:n1],s2[0:n2-i])) or (isScramble1(s1[0:i],s2[0:i]) and isScramble1(s1[i:n1],s2[i:n2])):
                    flag = True
                    break
            dic[key] = flag
            return flag
        return isScramble1(s1, s2)
