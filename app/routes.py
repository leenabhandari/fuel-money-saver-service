from app import app
from app import services
from flask import jsonify
from app import utils
from app import stubs
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Fuel-money saver Service"

@app.route('/fuel')
def main():
    pumps = stubs.pumps
    cost= utils.getCostList(pumps) 
    dist= utils.getDistList(pumps) 
    pumpCoordinates = utils.getCoordinates(pumps)
    n=len(cost)
    cap=300
    fuel=0
    print("Calculating...")
    final_output=services.getMinCost(cost,dist,n,cap,fuel,pumpCoordinates)
    return jsonify(final_output)

@app.route('/fuel', methods = ['POST'])
def mainPost():
    content = request.get_json()
    pumps = content['pumps']
    cost= utils.getCostList(pumps) 
    dist= utils.getDistList(pumps) 
    pumpCoordinates = utils.getCoordinates(pumps)
    n=len(cost)
    avgFuelRate = content['avgFuelRate']
    currentFuel = content['currentFuel']
    fuelCapacity = content['fuelCapacity']

    cap= utils.getCapacityDist(avgFuelRate,fuelCapacity)#content['capacity']
    fuel= utils.getFuelDist(avgFuelRate,currentFuel) #content['fuel']
    print("Calculating...")
    final_output=services.getMinCost(cost,dist,n,cap,fuel,pumpCoordinates)
    return jsonify(final_output)