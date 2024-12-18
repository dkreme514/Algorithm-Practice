"""
PC office capacity m = 2
Tallahassee office capacity n = 2
When problem complex, may help to think of sorting
"""
m=2
n=2
candidates = sorted(pairs,key=lambdax:abs(x[0]-x[1]))
panama = []
tally = []
while candidates and len(panama) < m and len(tally) < n:
    p,t=candidates.pop()
    if t < p:
        tally.append(t)
    else:
        panama.append(p)

while candidates and len(panama) < n:
    p,t=candidates.pop()
    panama.append(p)

while candidates and len(tally) < n:
    p,t=candidates.pop()
    tally.append(t)

return sum(panama) + sum(tally)