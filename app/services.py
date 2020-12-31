from app import utils
import requests

defaultFuelPrice = 85.21

def getPumpCosts(pumps):
    cost = []
    available_cities = "ahmedabad Ahmedabad  allahabad Allahabad  ambala Ambala  aurangabad Aurangabad  bangalore Bangalore  belgaum Belgaum  bhopal Bhopal  bhubaneswar Bhubaneswar  chandigarh Chandigarh  chennai Chennai  coimbatore Coimbatore  dehradun Dehradun  delhi Delhi  erode Erode  faridabad Faridabad  ghaziabad Ghaziabad  gulbarga Gulbarga  guntur Guntur  gurgaon Gurgaon  guwahati Guwahati  hyderabad Hyderabad  indore Indore  jaipur Jaipur  jalgaon Jalgaon  jammu Jammu  jamshedpur Jamshedpur  kakinada Kakinada  kannur Kannur  kanpur Kanpur  kolhapur Kolhapur  kolkata Kolkata  kozhikode Kozhikode  lucknow Lucknow  ludhiana Ludhiana  madurai Madurai  malappuram Malappuram  mangalore Mangalore  mumbai Mumbai  mysore Mysore  nagercoil Nagercoil  nagpur Nagpur  nashik Nashik  nellore Nellore  noida Noida  patna Patna  pondicherry Pondicherry  pune Pune  raipur Raipur  rajkot Rajkot  ranchi Ranchi  salem Salem  sangli Sangli  shimla Shimla  solapur Solapur  srinagar Srinagar  surat Surat  thane Thane  thanjavur Thanjavur  thiruvananthapuram Thiruvananthapuram  tirunelveli Tirunelveli  trichy Trichy  trivandrum Trivandrum  udupi Udupi  vadodara Vadodara  varanasi Varanasi  vellore Vellore  visakhapatnam Visakhapatnam  warangal Warangal  "

    for obj in pumps:
        city = obj['cityName']
        if available_cities.find(city) != -1:
            response = requests.get('https://mfapps.indiatimes.com/ET_Calculators/oilprice.htm?citystate=' + city)
            data = response.json()
            result = data['results']
            cost.append(float(result[0]['petrolPrice']))
            print(city + " : " + result[0]['petrolPrice'])
        else:
            cost.append(defaultFuelPrice)
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