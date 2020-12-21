# Honda Hackathon 2020
 
 https://honda-fuel-app.herokuapp.com/fuel

  **GET** - predefined input using stubs\
  **POST** - use the follow JSON input example
  
	  {"pumps" : [{
		"lat":15.4909,
		"lon":73.8278,
		"cost":82,
		"distToNext":115,
		"rate":1.1
	    },
	    {
		"lat":15.8497,
		"lon":74.4977,
		"cost":78,
		"distToNext":110,
		"rate":1
	    },
	    {
		"lat":16.7050,
		"lon":74.2433,
		"cost":90,
		"distToNext":230,
		"rate":1
	    },
	    {
		"lat":18.5204,
		"lon":73.8567,
		"cost":87,
		"distToNext":150,
		"rate":1
	    },
	    {
		"lat":19.0760,
		"lon":72.8777,
		"cost":91,
		"distToNext":280,
		"rate":1.1
	    },
	    {
		"lat":21.1702,
		"lon":72.8311,
		"cost":79,
		"distToNext":260,
		"rate":1
	    },
	    {
		"lat":23.0225,
		"lon":72.5714,
		"cost":82,
		"distToNext":215,
		"rate":1
	    },
	    {
		"lat":22.3039,
		"lon":70.8022,
		"cost":82,
		"distToNext":0,
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
