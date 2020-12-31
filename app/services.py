from app import utils
import requests

defaultFuelPrice = 85.21

def getPumpCosts(pumps):
    cost = []
    for obj in pumps:
        city = obj['cityName']
        response = requests.get('https://mfapps.indiatimes.com/ET_Calculators/oilprice.htm?citystate=' + city)
        data = response.json()
        result = data['results']
        if len(result) == 0:
            cost.append(defaultFuelPrice)
        else:
            cost.append(float(result[0]['petrolPrice']))
            print(city + " : " + result[0]['petrolPrice'])
    return cost


def getOriginalCost(cost,dist,cap,fuel,avgFuelRate):
    cur = 0
    ans = 0
    n = len(cost)
    while(cur<n-1):
        j=utils.getMaxJumpNode(cur,dist,cap)
        trip=utils.getDistTill(cur,j,dist)
        print("Original dist: " + str(trip) + " next: "+ str(j) + " current: " + str(cur))
        ans+=(cost[cur]*(cap - fuel))/avgFuelRate
        fuel=0
        cur = j
        print("Originally Cost: ",ans)
    return ans


def getMinCost(cost,dist,cap,fuel,pumpIds,avgFuelRate):
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
            val = (cost[i]*(cap-fuel))/avgFuelRate
            ans+= val
            expenditure[cur] = val
            fuel=0
            cur=j
        else:
            trip=utils.getDistTill(cur,i,dist)
            val = (cost[cur]*trip)/avgFuelRate
            ans+= val
            expenditure[cur] = val
            fuel=cap-utils.getDistTill(cur,i,dist)
            cur=i
        print("Cost: ",ans)
    pumps = []
    for i in expenditure:
        obj = pumpIds[i]
        obj.update({'spend': expenditure[i]})
        obj.update({'petrolRate': cost[i]})
        pumps.append(obj)
        
    res['pumpIds'] = pumps
    res['finalCost'] = ans
    originalCost = getOriginalCost(cost,dist,cap,fuel,avgFuelRate)
    res['originalCost'] = originalCost
    res['amtSaved'] = originalCost - ans
    return res