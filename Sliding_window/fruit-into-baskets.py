class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        basket={}
        left=right=0
        total=0
        while left<len(tree):
            if (right==len(tree)):
                total=max(total,sum(basket.values()))
                break
                
            if tree[right] in basket:
                basket[tree[right]]+=1
                right+=1
                continue
                
            if (tree[right] not in basket and len(basket)==2):
                total=max(total,sum(basket.values()))
                while True:
                    basket[tree[left]] -=1
                    if basket[tree[left]] == 0:
                        break
                    left += 1
                del basket[tree[left]]
                left+=1
                
            basket[tree[right]]=1
            right+=1
    
        return total   
                
            
        
