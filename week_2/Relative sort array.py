class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        correct=[]
        for i in arr2:
            count=0
            j=len(arr1)-1
            found=False
            num=0
            while j>=0:
                k=arr1[j]
                if i==k:
                    num=k
                    count+=1
                    arr1.pop(j)
                    found=True
                j-=1
            if found==True:
                correct.extend([num for z in range(count)])
        for x in range(len(arr1)):
            minimum=min(arr1)
            y=arr1.index(minimum)
            correct.append(minimum)
            arr1.pop(y)
        return correct
        
