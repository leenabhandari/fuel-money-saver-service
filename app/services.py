from app import utils

def getMinCost(cost,dist,n,cap,fuel,pumpCoordinates):
    res = {}
    ans=0
    cur=0
    expenditure={}
    while(cur<n-1):
        j=utils.getMaxJumpNode(cur,dist,cap)
        i=utils.getNextMinNode(j,cur,cost)
        print("Distance:",j,"next:",i,"current:",cur,"fuel: ",fuel)
        expenditure[i] = 0
        if(i==cur):
            ans+=cost[i]*(cap-fuel)
            expenditure[i] = cost[i]*(cap-fuel)
            fuel=cap-utils.getDistTill(cur,j,dist)
            cur=j
        else:
            trip=utils.getDistTill(cur,i,dist)
            ans+=cost[cur]*trip
            expenditure[i] = cost[cur]*trip
            fuel=0
            cur=i
        print("Cost",ans)
    coordinates = []
    for i in expenditure:
        obj = pumpCoordinates[i]
        obj.update({'spend': expenditure[i]})
        coordinates.append(obj)
        
    res['coordinates'] = coordinates
    res['finalCost'] = ans
    return res