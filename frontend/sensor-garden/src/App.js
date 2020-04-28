import React from 'react';
import SpecificSensorData from './services/sensorDataSpecific.js' 
import {ApolloClient, ApolloLink} from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';
import { InMemoryCache } from "apollo-cache-inmemory";
import { HttpLink } from "apollo-link-http";
import Clock from './clock.js'; 

const cache = new InMemoryCache();

const link = new HttpLink({
  uri: "https://tomato-sensor.ue.r.appspot.com/"
});

const client = new ApolloClient({
  link,
  cache
});

 function App() {
  
  return (
      <div className="App">
        <section className="hero is-primary">
          <div className="hero-body">
            <div className="container">
              <h1 className="title">Sensor Garden</h1>
              <h2 className="subtitle">  
                <Clock></Clock>
              </h2>
            </div>   
          </div>
        </section>
      <ApolloProvider client={client}>
      <section className="hero">
      <div className="hero-body">            
          <div className="tile is-ancestor">
          <div className="tile is-parent">
        <SpecificSensorData sensorId="soil_moisture_plant_1"></SpecificSensorData>
        <SpecificSensorData sensorId="soil_moisture_plant_2"></SpecificSensorData>
        <SpecificSensorData sensorId="ambient_humidity"></SpecificSensorData>
        <SpecificSensorData sensorId="ambient_temp"></SpecificSensorData>
        <SpecificSensorData sensorId="ambient_pressure"></SpecificSensorData>
        <SpecificSensorData sensorId="soil_temp_plant_1"></SpecificSensorData>
        </div>
        </div>
    </div>
</section>
      </ApolloProvider>
      </div>
    );
}
export default App;