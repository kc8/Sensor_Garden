package main

import (
	"errors"
	"log"
)

type SensorData struct {
	measurement float32
	name        string
	unit        string
	id          SensorId
}

type SensorId struct {
	id string
}

type Sensors struct {
	sensors map[SensorId]SensorData
}

func (sd *Sensors) Update(sensor SensorData) bool {
	sensorMapped, isSensorInMap := sd.sensors[sensor.id]

	if isSensorInMap == true {
		sd.sensors[sensor.id] = sensor

		if sensorMapped.id != sensor.id {
			log.Println("[WARN] Received a differeing sensor name from client...")
		}

		if sensorMapped.unit != sensor.unit {
			log.Println("[WARN] Received a differeing unit name from client...")
		}
		return true
	}
	return false
}

func (sd *Sensors) GetSensorData(sensorId SensorId) (SensorData, error) {
	sensorMapped, isSensorInMap := sd.sensors[sensorId]
	if isSensorInMap == true {
		return sensorMapped, nil
	}
	// TODO can we return something else besides the empty struct here?
	return SensorData{}, errors.New("Sensor does not exist")
}

func (sd *Sensors) InitSensors(sensorIds []string, size int) {
	sd.sensors = make(map[SensorId]SensorData, size)
	for i := 0; i < size; i++ {
		var currentSensor = sensorIds[i]
		id := SensorId{id: currentSensor}
		unit := ""

		sd.sensors[id] = SensorData{
			id:          id,
			measurement: 0.0,
			unit:        unit,
			name:        "",
		}
	}
}
