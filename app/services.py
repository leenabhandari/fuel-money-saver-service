from app import utils


def getOriginalCost(cost,dist,cap,fuel):
    cur = 0
    ans = 0
    n = len(cost)
    while(cur<n-1):
        j=utils.getMaxJumpNode(cur,dist,cap)
        trip=utils.getDistTill(cur,j,dist)
        ans+=cost[cur]*trip
        fuel=0
        cur = j
        print("Originally Cost: ",ans)
    return ans


def getMinCost(cost,dist,cap,fuel,pumpCoordinates):
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
            fuel=cap-utils.getDistTill(cur,j,dist)
            cur=j
        else:
            trip=utils.getDistTill(cur,i,dist)
            ans+=cost[cur]*trip
            expenditure[cur] = cost[cur]*trip
            fuel=0
            cur=i
        print("Cost: ",ans)
    coordinates = []
    for i in expenditure:
        obj = pumpCoordinates[i]
        obj.update({'spend': expenditure[i]})
        coordinates.append(obj)
        
    res['coordinates'] = coordinates
    res['finalCost'] = ans
    return res