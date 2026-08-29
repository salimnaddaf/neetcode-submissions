class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+"#"
            for ch in s:
                result+=ch+"#"
        return result


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        counter=0
        while i<len(s):
            while s[i]!='#':
                counter=counter*10+int(s[i])
                i+=1
            curr=""
            i+=1
            while counter>0 and i<len(s) and s[i]!='#':
                curr+=s[i]
                i+=2
                counter-=1
            result.append(curr)
        return result
                
