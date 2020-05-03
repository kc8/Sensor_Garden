import React from 'react'
import SpecificSensorData from './sensorDataSpecific.js'

function SensorGroup() {

    return (
        <div>
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
            <SpecificSensorData sensorId="soil_temp_plant_2"></SpecificSensorData>
            </div>
          </div>
        </div>
      </section>

        </div>
    )
}

export default SensorGroup;