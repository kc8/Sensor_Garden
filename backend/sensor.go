package main

import (
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
    fmt.Println(sensorMapped);
    fmt.Println(isSensorInMap);

	if isSensorInMap == true {
		sensorMapped.measurement = sensor.measurement

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
