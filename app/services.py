from app import utils


def getOriginalCost(cost,dist,cap,fuel,avgFuelRate):
    cur = 0
    ans = 0
    n = len(cost)
    while(cur<n-1):
        j=utils.getMaxJumpNode(cur,dist,cap)
        trip=utils.getDistTill(cur,j,dist)
        print(trip)
        ans+=cost[cur]*trip
        fuel=0
        cur = j
        print("Originally Cost: ",ans/avgFuelRate)
    return ans/avgFuelRate


def getMinCost(cost,dist,cap,fuel,pumpCoordinates,avgFuelRate):
    res = {}
    ans=0
    cur=0
    n = len(cost)
    expenditure={}
    while(cur<n-1):
        j=utils.getMaxJumpNode(cur,dist,cap)
        i=utils.getNextMinNode(j,cur,cost)
        print("Distance:",j,"next:",i,"current:",cur,"fuel: ",fuel)
        expenditure[cur] = 0
        if(i==cur):
            ans+=cost[i]*(cap-fuel)
            expenditure[cur] = cost[i]*(cap-fuel)
            fuel=0
            cur=j
        else:
            trip=utils.getDistTill(cur,i,dist)
            ans+=cost[cur]*trip
            expenditure[cur] = cost[cur]*trip
            fuel=cap-utils.getDistTill(cur,i,dist)
            cur=i
        print("Cost: ",ans)
    coordinates = []
    for i in expenditure:
        obj = pumpCoordinates[i]
        obj.update({'spend': expenditure[i]})
        coordinates.append(obj)
        
    ans = ans/avgFuelRate
    res['coordinates'] = coordinates
    res['finalCost'] = ans
    originalCost = getOriginalCost(cost,dist,cap,fuel,avgFuelRate)
    res['originalCost'] = originalCost
    res['amtSaved'] = originalCost - ans
    return res