# Smart Fuel Money Saver
 
 ### Ranked under Top 10 projects in the Honda Hackathon 2020
 
 https://honda-fuel-app.herokuapp.com/fuel

  **GET** - predefined input using stubs\
  **POST** - use the follow JSON input example
  
	 {"pumps" : [{
		"id":1,
		"distToNext":117.69,
		"totalDuration":934,
		"trafficDelay":98,
		"cityName":"Mumbai",
		"rate":1
	    },
	    {
		"id":2,
		"distToNext":104.70,
		"totalDuration":767,
		"trafficDelay":92,
		"cityName":"Panchshil",
		"rate":1
	    },
	    {
		"id":3,
		"distToNext":113.06,
		"totalDuration":556,
		"trafficDelay":83,
		"cityName":"Lonavla",
		"rate":1
	    },
	    {
		"id":4,
		"distToNext":100.87,
		"totalDuration":323,
		"trafficDelay":7,
		"cityName":"Dattwadi",
		"rate":1
	    },
	    {
		"id":5,
		"distToNext":101.96,
		"totalDuration":328,
		"trafficDelay":28,
		"cityName":"Panshil",
		"rate":1.1
	    },
	    {
		"id":6,
		"distToNext":100.45,
		"totalDuration":316,
		"trafficDelay":10,
		"cityName":"Pune",
		"rate":1
	    },
	    {
		"id":7,
		"distToNext":102.13,
		"totalDuration":310,
		"trafficDelay":15,
		"cityName":"Vichumbe",
		"rate":1
	    },
	    {
		"id":8,
		"distToNext":0,
		"totalDuration":327,
		"trafficDelay":33,
		"cityName":"Navi Mumbai",
		"rate":1
	    }],
	    "avgFuelRate": 16,
	    "currentFuel": 0,
	    "fuelCapacity":40
	}

**https://docs.google.com/presentation/d/1ITZGMWD5aCPoYGCXkdq11kH2GLRLGWJfUL3g-0c7p_Q/edit?usp=sharing** \
**DEMO - https://drive.google.com/file/d/1oPJhf3JBVJnyz305ymajk1dx4901m1Oi/view** \
**APK - https://drive.google.com/file/d/11gZvyWVkwp9TsN7cHFqQMwsRkkSQH2cb/view?usp=sharing** 
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
