class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap={}
        for s in strs:
            chList=[0]*26
            for ch in s:
                chList[ord(ch)-ord('a')]+=1
            key=tuple(chList)
            if key not in anagramMap:
                anagramMap[key]=[]
            anagramMap[key].append(s)
        return list(anagramMap.values())