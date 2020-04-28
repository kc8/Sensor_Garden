from graphene import ObjectType, String, Schema, List, ResolveInfo
from google.cloud import firestore
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_graphql import GraphQLView

class MeasurmentValues(ObjectType): 
    sensor_name = String()
    sensor_measurement = String()


class SpecificSensors(ObjectType): 
    common_name = String()
    measurement_friendly = String()
    measurement_precise = String()
    sensor_id = String()
    units_of_measure = String()


class Query(ObjectType): 
    
    measurements = List(MeasurmentValues)
    measurements_specific_values = List(SpecificSensors, sensor_id=String(default_value="None"))
    test_with_arg = String(arg=String(default_value="Return Me"))
    test = String()

    def resolve_measurements_specific_values(self, info: ResolveInfo, sensor_id):
        """
        Returns the specific data from the specific document that was queried
        Example query: ' 
                query {measurementsSpecificValues(sensorId:"ambient_humidity",) {
                    commonName
                    measurementFriendly
                    measurementPrecise
                    sensorId
                    unitsOfMeasure
            }}
        '
        """
        # if sensor_id == "None": 
        #     return "You did not enter a query name"
        doc_ref = firestore.Client().collection("tom_plant_sensor_readings").document(sensor_id) #Do we need to sanatize this value? 
        doc = doc_ref.get()
        data = doc.to_dict()

        return [data]


    def resolve_measurements(self, info: ResolveInfo): 
        """
        Returns all the data from the "readings" doc which contains all sensor data with an ID and raw measurement
        Example query:
                'query {
                    measurements {
                        sensorName
                        sensorMeasurement
                    }
                }'
        
        """
        doc_ref = firestore.Client().collection("tom_plant_sensor_readings").document("readings")
        doc = doc_ref.get()
        data = doc.to_dict()

        measurement_value_obj_list = []

        for key, value in data.items(): 
            measurement = MeasurmentValues(key, value)
            measurement_value_obj_list.append(measurement)

        return measurement_value_obj_list
    
    def resolve_test_with_arg(self, info, arg):
        """
        Used for testing a query with an arg to make sure all is working. 
        Example:'{testWithArg(arg:"Test")}'
        """ 
        return f"Returning {arg} as a string"

    def resolve_test(self, info):
        return "Returning a test String"


def get_sensor_data(sensor):
    """
    OLD AND WILL REMOVE WHEN ITS TIME
    Duplicated because we want to get rid of the all but only after we refine our query a little more"""

    sensor_names = [
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp",
        "ambient_humidity",
        "ambient_pressure",
        "all"
    ]

    doc_ref = firestore.Client().collection("tom_plant_sensor_readings").document("readings")
    doc = doc_ref.get()
    data = doc.to_dict()
    result_data = {}
    if sensor in sensor_names:
        if sensor == 'all': 
            result_data = data
        else: 
            result_data = data[sensor]
    return result_data


app = Flask(__name__)
schema = Schema(query=Query)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.add_url_rule(
    '/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.route('/')
def main(request=None):
    # Some test queries:
    pass


if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=8080)

