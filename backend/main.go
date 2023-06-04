package main

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

type Services struct {
	sensors Sensors
}

type RawSensorData struct {
	SensorName string  `'json:"sensorName"`
	Id         string  `'json:"id"`
	Status     string  `'json:"status"`
	Unit       string  `'json:"unit"`
	Measurment float32 `'json:"measurment"`
}

type RawSensors struct {
	Sensors []RawSensorData `'json:"sensors"`
}

func (s *Services) getAvailSensors(g *gin.Context) {
}

// NOTE auth!
func (s *Services) waterSensorData(g *gin.Context) {
}

func (s *Services) populateTheSensors(g *gin.Context) {
	var json RawSensors
	isBound := g.ShouldBindJSON(&json)

	if isBound != nil {
		g.JSON(http.StatusBadRequest, gin.H{"RECEIEVED INVALID REQUEST": isBound.Error()})
		return
	}
	if s.sensors.sensors != nil {
		g.JSON(http.StatusBadRequest, gin.H{
			"Failed to init sensors": "Senseors already initilized. Please add instead",
		})
		return
	}

	sensorLen := len(json.Sensors)
	if sensorLen <= 0 {
		g.JSON(http.StatusBadRequest, gin.H{
			"Failed to update sensors": "Request did not contain a list of sensors to update",
		})
		return
	}
	s.sensors.sensors = make(map[SensorName]SensorData, 10)
	for i := 0; i < sensorLen; i++ {
		var currentSensor = json.Sensors[i]
		name := SensorName{name: currentSensor.SensorName}
		measurement := currentSensor.Measurment
		unit := currentSensor.Unit
		s.sensors.sensors[name] = SensorData{
			name:        name,
			measurement: measurement,
			unit:        unit,
		}

	}
	g.JSON(http.StatusOK, gin.H{"Sesnor Data populated": true})
}

func (s *Services) updateSensorData(g *gin.Context) {
	var json RawSensors
	isBound := g.ShouldBindJSON(&json)

	if isBound != nil {
		log.Println("[WARN] Received invalid json for /sendData", isBound.Error())
		g.JSON(http.StatusBadRequest, gin.H{"RECEIEVED INVALID REQUEST": isBound.Error()})
		return
	}

	sensorLen := len(json.Sensors)
	if sensorLen <= 0 {
		g.JSON(http.StatusBadRequest, gin.H{
			"Failed to update sensors": "Request did not contain a list of sensors to update",
		})
		log.Println("[WARN] Received invalid length of sensors for sendData")
		return
	}
	for i := 0; i < sensorLen; i++ {
		var currentSensor = json.Sensors[i]
		name := SensorName{name: currentSensor.SensorName}
		measurement := currentSensor.Measurment
		unit := currentSensor.Unit

		sensorData := SensorData{
			measurement: measurement,
			name:        name,
			unit:        unit,
		}
		currentStatus := s.sensors.Update(sensorData)
        log.Println("[INFO] Received request to update sensor with the following", sensorData);

		// TODO don't fail right away, update sensors that are valid and
		// then return states for each sensor updated
		if currentStatus == false {
			g.JSON(http.StatusOK, gin.H{"Update Sensor Data": currentStatus})
			return
		}
	}
	g.JSON(http.StatusOK, gin.H{"Update Sensor Data": true})
}

func (s *Services) getAvailableSensors(g *gin.Context) {
}

func (s *Services) getSensorData(g *gin.Context) {
	sensorName := g.Query("sensorName")
	data, err := s.sensors.GetSensorData(SensorName{name: sensorName})
	if err != nil {
		g.JSON(http.StatusBadRequest, gin.H{"Could not find sensor": sensorName})
		return
	}
    serializedData := RawSensorData{
		SensorName: data.name.name,
		Id:         "",
        Status:     "",
        Unit: data.unit,
		Measurment: data.measurement,
	}

	g.JSON(http.StatusOK, serializedData)
	return
}

func main() {
	gin.SetMode(gin.ReleaseMode)
	r := gin.New()
	r.Use(AuthWrapper())
	services := Services{}

    // since our rpi-drivers are messy.. for now I just want to update them here
    sensorNames := []string{
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
        "ambient_temp",
        "ambient_humidity",
        "ambient_pressure"}
    services.sensors.InitSensors(sensorNames, len(sensorNames))

	r.POST("/sendData", services.updateSensorData)
	r.POST("/populateTheSensorsFromDevice", services.populateTheSensors)
	r.GET("/getSensorData", services.getSensorData)

	r.Run(":8080")
}
