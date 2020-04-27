from graphene import ObjectType, String, Schema, List, ResolveInfo
from google.cloud import firestore
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_graphql import GraphQLView

class MeasurmentValues(ObjectType): 
    sensor_name = String()
    sensor_measurement = String()

class Query(ObjectType): 
    
    measurements = List(MeasurmentValues)

    def resolve_measurements(self, info: ResolveInfo): 
        sensor_names = get_sensor_value_dict()
    
        measurement_value_obj_list = []

        for key, value in sensor_names.items(): 
            measurement = MeasurmentValues(key, value)
            measurement_value_obj_list.append(measurement)

        return measurement_value_obj_list
        

def get_sensor_value_dict(): 

    doc_ref = firestore.Client().collection("tom_plant_sensor_readings").document("readings")
    doc = doc_ref.get()
    data = doc.to_dict()
    return data


def get_sensor_data(sensor):
    """Duplicated because we want to get rid of the all but only after we refine our query a little more"""

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

class Query_old(ObjectType): 
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    sensor_data = String(sensor=String(default_value="all"))

    def resolve_sensor_data(root, info, sensor):
        _data = get_sensor_data(sensor)
        return _data


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
    query_string = '{hello(name: "John")}'
    result = schema.execute(query_string)
    data = result.data['hello']


if __name__ == '__main__': 
    app.run(host='127.0.0.1', port=8080)

