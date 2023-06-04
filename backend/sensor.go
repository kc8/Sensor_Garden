package main

import (
	"errors"
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
	if isSensorInMap == true {
		return sensorMapped, nil
	}
	// TODO can we return something else besides the empty struct here?
	return SensorData{}, errors.New("Sensor does not exist")
}

func (sd *Sensors) InitSensors(sensorNames []string, size int) {
	sd.sensors = make(map[SensorName]SensorData, size)
	for i := 0; i < size; i++ {
		var currentSensor = sensorNames[i]
		name := SensorName{name: currentSensor}
		unit := ""

		sd.sensors[name] = SensorData{
			name:        name,
			measurement: 0.0,
			unit:        unit,
		}
	}
}
