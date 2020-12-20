
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

def getDistList(pumps):
    dist = []
    for obj in pumps:
        dist.append(obj['distToNext'] * obj['multiplier'])
    dist.pop()
    return dist

def getCoordinates(pumps):
    coordinates = []
    for obj in pumps:
        coordinates.append({
            'lat': obj['lat'],
            'lon': obj['lon']
        })
    return coordinates

def getCapacityDist(avgFuelRate,fuelCapacity):
    return avgFuelRate * fuelCapacity

def getFuelDist(avgFuelRate, currentFuel):
    return avgFuelRate * currentFuel
