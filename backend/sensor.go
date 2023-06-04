package main

import (
	"errors"
	"fmt"
	"log"
)

type SensorData struct {
	measurement float32
	name        SensorName
	unit        string
}

type SensorName struct {
	name string
}

type Sensors struct {
	sensors map[SensorName]SensorData
}

func (sd *Sensors) Update(sensor SensorData) bool {
	sensorMapped, isSensorInMap := sd.sensors[sensor.name]

	if isSensorInMap == true {
		sd.sensors[sensor.name] = sensor 

		if sensorMapped.name != sensor.name {
			log.Println("[WARN] Received a differeing sensor name from client...")
		}

		if sensorMapped.unit != sensor.unit {
			log.Println("[WARN] Received a differeing unit name from client...")
		}
		return true
	}
	return false
}

func (sd *Sensors) GetSensorData(sensorName SensorName) (SensorData, error) {
	sensorMapped, isSensorInMap := sd.sensors[sensorName]
    fmt.Println("get", sensorMapped.measurement);
	if isSensorInMap == true {
		return sensorMapped, nil
	}
    // TODO can we return something else besides the empty struct here?
	return SensorData{}, errors.New("Sensor does not exist")
}
