def gridlandMetro(n, m, k, track):
    summ=n*m
    visited={}

    for j in track:
        overlap=False
        if j[0] in visited:
            for x in range(len(visited[j[0]])):
                current=visited[j[0]][x]
                if not (j[2] < current[0] or j[1] > current[1]):
                    current[0],current[1]=min(j[1],current[0]),max(j[2],current[1])
                    overlap=True
                    break
            if not overlap:
                visited[j[0]].append([j[1],j[2]])
            continue
        visited[j[0]]=[[j[1],j[2]]]
    for i in visited:
        for j in visited[i]:
            summ-=(j[1]-j[0]+1)
    return summ
