# Honda Hackathon 2020
 
 https://honda-fuel-app.herokuapp.com/fuel

  **GET** - predefined input using stubs\
  **POST** - use the follow JSON input example
  
	 {"pumps" : [{
		"id":1,
		"cost":82,
		"distToNext":117.69,
		"totalDuration":934,
		"trafficDelay":98,
		"rate":1
	    },
	    {
		"id":2,
		"cost":78,
		"distToNext":104.70,
		"totalDuration":767,
		"trafficDelay":92,
		"rate":1
	    },
	    {
		"id":3,
		"cost":90,
		"distToNext":113.06,
		"totalDuration":556,
		"trafficDelay":83,
		"rate":1
	    },
	    {
		"id":4,
		"cost":87,
		"distToNext":100.87,
		"totalDuration":323,
		"trafficDelay":7,
		"rate":1
	    },
	    {
		"id":5,
		"cost":91,
		"distToNext":101.96,
		"totalDuration":328,
		"trafficDelay":28,
		"rate":1.1
	    },
	    {
		"id":6,
		"cost":79,
		"distToNext":100.45,
		"totalDuration":316,
		"trafficDelay":10,
		"rate":1
	    },
	    {
		"id":7,
		"cost":82,
		"distToNext":102.13,
		"totalDuration":310,
		"trafficDelay":15,
		"rate":1
	    },
	    {
		"id":8,
		"cost":82,
		"distToNext":0,
		"totalDuration":327,
		"trafficDelay":33,
		"rate":1
	    }],
	    "avgFuelRate": 16,
	    "currentFuel": 0,
	    "fuelCapacity":40
	}

https://docs.google.com/presentation/d/1ITZGMWD5aCPoYGCXkdq11kH2GLRLGWJfUL3g-0c7p_Q/edit?usp=sharing

## Algorithm

	getOptimizedFuelPlan(currentFuel, avgFuelDistance, maxTankCapacity, stations):
		currentStation= 0 //startingPoint
		currentFuel = fuelInTank
	
		while currentStation < endPoint:
			estimatedPrice = 0
			distanceCanTravel = currentFuel * avgFuelDistance
			j = getMaxDistanceNode()
			minPriceNode = getMinPriceNodeUntilJ(j)
			if minPriceNode = currentStation:
				currentStation = j
				estimatedPrice += calculateTripPrice()
				updateCurrentFuel()
			else:
				currentStation = minPriceNode
				estimatedPrice += calculateTripPrice()
				updateCurrentFuel()
			fuelStations.append(currentStation)
			addTripCostToStation()

		return estimatedPrice,fuelStations
