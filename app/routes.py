from app import app
from app import services
from flask import jsonify
from app import utils
from app import stubs
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Fuel-money saver Service to save money spent on fuel on long trips. Endpoint: /fuel . Use GET for predefined inputs and POST for custom input."

@app.route('/fuel')
def main():
    pumps = stubs.pumps
    #cost= utils.getCostList(pumps) 
    cost = services.getPumpCosts(pumps)
    dist= utils.getDistList(pumps) 
    pumpCoordinates = utils.getPumpIds(pumps)
    avgFuelRate = stubs.avgFuelRate
    currentFuel = stubs.currentFuel
    fuelCapacity = stubs.fuelCapacity
    cap= utils.getCapacityDist(avgFuelRate,fuelCapacity)
    fuel= utils.getFuelDist(avgFuelRate,currentFuel) 
    final_output=services.getMinCost(cost,dist,cap,fuel,pumpCoordinates,avgFuelRate)
    return jsonify(final_output)

@app.route('/fuel', methods = ['POST'])
def mainPost():
    content = request.get_json()
    pumps = content['pumps']
    #cost= utils.getCostList(pumps) 
    cost = services.getPumpCosts(pumps)
    dist= utils.getDistList(pumps) 
    print(dist)
    pumpIds = utils.getPumpIds(pumps)
    avgFuelRate = content['avgFuelRate']
    currentFuel = content['currentFuel']
    fuelCapacity = content['fuelCapacity']

    cap= utils.getCapacityDist(avgFuelRate,fuelCapacity)
    fuel= utils.getFuelDist(avgFuelRate,currentFuel) 
    final_output=services.getMinCost(cost,dist,cap,fuel,pumpIds,avgFuelRate)
    return jsonify(final_output)