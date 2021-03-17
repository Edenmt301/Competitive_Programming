class Solution:
    
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        new=""
        
        for i in range(len(S)):
            sh = sum(shifts[i:]) % 26
            if ord(S[i]) + sh > ord('z'):
                z=(ord(S[i]) + sh) - ord('z')
                new+= (chr(ord('a') + z -1))
                continue
            new += str(chr(ord(S[i]) + sh))
        return new
