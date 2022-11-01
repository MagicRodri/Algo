def get_min(d = None):
    index = 1
    mini = d[1]['ra']
    for i in d :
        if d[i]['ra'] < mini:
            mini = d[i]['ra']
            index = i
    return index

def get_max(d = None):
    index = 1
    maxi = d[1]['ra']
    for i in d :
        if d[i]['ra'] > maxi:
            maxi = d[i]['ra']
            index = i
    return index


n , m , q = list(map(int,input().split()))

datacenters = dict()

for i in range(1,n+1):
    datacenters[i] = {
        'r' : 0,
        'a' : [j for j in range(1,m+1)],
        'm' : m,
        'ra' : 0
	}
    
results = []
for _ in range(q):
    event = input().split()
    if event[0] == 'GETMIN':
        results.append(get_min(datacenters))
    elif event[0] == 'GETMAX':
        results.append(get_max(datacenters))
    elif event[0] == 'RESET':
        i = int(event[1])
        datacenters[i]['r'] += 1
        datacenters[i]['a'] =[j for j in range(1,m+1)]
        datacenters[i]['m'] = m
        datacenters[i]['ra'] = datacenters[i]['r'] * datacenters[i]['m']
    elif event[0] == 'DISABLE':
        i,j = int(event[1]), int(event[2])
        if j in datacenters[i]['a']:
            datacenters[i]['a'].remove(j)
            datacenters[i]['m'] -= 1
            datacenters[i]['ra'] = datacenters[i]['r'] * datacenters[i]['m']
    
for r in results:
    print(r)
    
# datacenter = {
#     'm' : 3,
#     'a' : 0,
    
# }
