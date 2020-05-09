/*
This component queries for all of the different sensor values. 
Each sensor is its own value incase there is an error with getting the value
*/
import React from 'react'
import GetSensorData from './sensorDataTesting.js'
import { ApolloProvider } from '@apollo/react-hooks';
import ApolloClient from 'apollo-boost';
import { InMemoryCache} from "apollo-cache-inmemory";


const cache = new InMemoryCache();

const defaultOptions  = {
    watchQuery: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'ignore',
    },
    query: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'all',
    },
  }

const client = new ApolloClient({
  uri: "https://tomato-sensor.ue.r.appspot.com/",
  cache,
  DefaultOptions: defaultOptions
});

/*TO-DO: Look for a better way to render GetSensorData.
   Create Array of sensors and pass it with map() into the GetSensorData function? 
*/
function SensorGroup() {

    return (
        <div>
        <ApolloProvider client={client}>
        <section className="hero">
          <div className="hero-body">            
            <div className="tile is-ancestor">
              <div className="tile is-parent">
              <GetSensorData sensorId="soil_moisture_plant_1"></GetSensorData>
              <GetSensorData sensorId="soil_moisture_plant_2"></GetSensorData>
              <GetSensorData sensorId="ambient_humidity"></GetSensorData>
              <GetSensorData sensorId="ambient_temp"></GetSensorData>
              <GetSensorData sensorId="ambient_pressure"></GetSensorData>
              <GetSensorData sensorId="soil_temp_plant_1"></GetSensorData>
              <GetSensorData sensorId="soil_temp_plant_2"></GetSensorData>
              </div>
            </div>
          </div>
        </section>
        </ApolloProvider>
      </div>
    )
}

export default SensorGroup;