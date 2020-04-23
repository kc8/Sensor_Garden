"""
Gets the sensor data from the firestore

List of sensor names to retrieve:
"""

def retrieve_data(sensor_name):
    """Retrieves the data from the firestore"""
    return f"Sensor data and message {sensor_name}"


def main(request):
    sensor_names = [
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp",
        "ambient_humidity",
        "ambient_pressure",
    ]
    json_data = request.get_json()
    sensor_to_get = json_data['sensor']
    
    if sensor_to_get in sensor_names: 
        retrieve_data(sensor_to_get)
    else: 
        return f"Not Found"