class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        baskets={}
        for i in s:
            if i in baskets:
                baskets[i]+=1
            else:
                baskets[i]=1
        for i in t:
            if i not in baskets or baskets[i]==0:
                return False
            baskets[i]-=1
        return True