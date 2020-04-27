"""
Gets the sensor data from the firestore

List of sensor names to retrieve:
"""
import json
from google.cloud import firestore
from flask import jsonify


def main(requset):
    sensor_names = [
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp",
        "ambient_humidity",
        "ambient_pressure",
    ]

    doc_ref = firestore.Client().collection("tom_plant_sensor_readings").document("readings")
    doc = doc_ref.get()
    data = doc.to_dict()
    response = jsonify(data)
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response

    ### UNSED VARIABLES FOR FUTURE USE ###
    #json_data = request.get_json()
    #sensor_to_get = json_data['sensor']
    #return sensor_to_get
    #if sensor_to_get in sensor_names: 
    


