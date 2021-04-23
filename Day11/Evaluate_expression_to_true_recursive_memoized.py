class Solution:
    # @param A : string
    # @return an integer
    
    def cnttrue(self, A):
        dic = {}
        n = len(A)-1
        
        def solve(i,j,isTrue):
            if i>j:
                return 0
            elif i==j:
                if isTrue == True:
                    if A[i]=="T":
                        return 1
                    else:
                        return 0
                else:
                    if A[i]=="F":
                        return 1
                    else:
                        return 0
            ans = 0
            key = str(i)+" " +str(j)+" "+str(isTrue)
            if key in dic:
                return dic[key]
            for k in range(i+1,j,2):
                LT = solve(i,k-1,True)
                RT = solve(k+1,j,True)
                LF = solve(i,k-1,False)
                RF = solve(k+1,j,False)
                #print(LT,RT,LF,RF)
                
                if A[k]=="|":
                    if isTrue:
                        ans += LT*RF + LF*RT + LT*RT
                    else:
                        ans += LF*RF
                elif A[k] == "&":
                    if isTrue:
                        ans += LT*RT
                    else:
                        ans += LT*RF + LF*RT + LF*RF
                elif A[k]=="^":
                    if isTrue:
                        ans += LT*RF + LF*RT
                    else:
                        ans += LT*RT + LF*RF
            dic[key] = ans
            return ans            
        
        ans = solve(0,n,True)
        return ans
                        
                
