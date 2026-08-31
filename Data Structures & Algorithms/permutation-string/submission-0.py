class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charsS1 = {}
        for s in s1:
            charsS1[s] = charsS1.get(s,0)+1
        left = 0
        for right in range(len(s2)):
            if s2[right] in charsS1 and charsS1[s2[right]] > 0:
                charsS1[s2[right]]-=1
                if max(charsS1.values()) == 0:
                    return True
            else:
                if s2[right] not in charsS1 or charsS1[s2[right]]==0:
                    while left < right:
                        if s2[left] in charsS1:
                            charsS1[s2[left]]+=1
                        left+=1
        return False
        