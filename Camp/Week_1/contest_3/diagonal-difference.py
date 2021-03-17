def diagonalDifference(arr):
    p_curr=[0,0]
    s_curr=[0,len(arr)-1]
    if not arr:
        return 
    diag_sum=[arr[p_curr[0]][p_curr[1]],arr[s_curr[0]][s_curr[1]]]
    
    for i in range(len(arr)-1):
        p_curr[0]+=1
        p_curr[1]+=1
        s_curr[0]+=1
        s_curr[1]-=1
        diag_sum[0]+=arr[p_curr[0]][p_curr[1]]
        diag_sum[1]+=arr[s_curr[0]][s_curr[1]]
    summ=abs(diag_sum[0]-diag_sum[1])
    return summ
