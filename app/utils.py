
def getMaxJumpNode(cur,dist,cap):
    limit=0
    while(cur<=len(dist)-1 and limit+dist[cur]<=cap):
        limit+=dist[cur]
        cur=cur+1
    return cur

def getNextMinNode(j,cur,cost):
    mini=cur
    price=cost[cur]
    while(cur<=j):
        if(cost[cur]<price):
            mini=cur
            price=cost[cur]
        cur=cur+1
    return mini

def getDistTill(cur,i,dist):
    ans=0
    while(cur!=i):
        ans+=dist[cur]
        cur=cur+1
    return ans

def getCostList(pumps):
    cost = []
    for obj in pumps:
        cost.append(obj['cost'])
    return cost

def getDistList(pumps,fuel):
    dist = []
    for obj in pumps:
        calcDist = obj['distToNext']
        distWithTraffic = (obj['trafficDelay'] * obj['distToNext'] / obj['totalDuration'] ) + calcDist
        distWithOtherFactors = distWithTraffic * obj['rate']
        print(distWithOtherFactors)
        dist.append(distWithOtherFactors)

    dist.pop()

    i = 0
    while(i<len(dist) and dist[i]<=fuel):
        fuel = fuel - dist[i]
        dist[i] = 0
        i = i + 1
    if(i<len(dist)):
        dist[i] = dist[i] - fuel
    return dist

def getPumpIds(pumps):
    coordinates = []
    for obj in pumps:
        coordinates.append({
            'id': obj['id']
        })
    return coordinates

def getFuelDist(avgFuelRate, currentFuel):
    return avgFuelRate * currentFuel
