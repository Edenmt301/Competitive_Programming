class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes={}
        ids={}
        answer=[0]*k
        for i in logs:
            if i[1] in minutes:
                if i[0] not in ids:
                    ids[i[0]]=1
                    minutes[i[1]].add(i[0])
                elif i[0] not in minutes[i[1]]:
                    minutes[i[1]].add(i[0])
                    ids[i[0]]+=1
                continue
            minutes[i[1]]={i[0]}
            if i[0] not in ids:
                ids[i[0]]=1
            else:
                 ids[i[0]]+=1
        
        for j in ids:
            if ids[j] <= k:
                answer[ids[j]-1]+=1
        return answer
        
        
