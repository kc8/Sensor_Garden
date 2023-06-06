package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gin-contrib/cors"
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
		g.JSON(http.StatusBadRequest, gin.H{"RECEIVED INVALID REQUEST": isBound.Error()})
		return
	}
	if s.sensors.sensors != nil {
		g.JSON(http.StatusBadRequest, gin.H{
			"Failed to init sensors": "Sensors already inited. Please add instead",
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
	s.sensors.sensors = make(map[SensorId]SensorData, 10)
	for i := 0; i < sensorLen; i++ {
		var currentSensor = json.Sensors[i]
		id := SensorId{id: currentSensor.Id}
		measurement := currentSensor.Measurment
		unit := currentSensor.Unit
		s.sensors.sensors[id] = SensorData{
			name:        currentSensor.SensorName,
			measurement: measurement,
			unit:        unit,
			id:          id,
		}

	}
	g.JSON(http.StatusOK, gin.H{"Sesnor Data populated": true})
}

func (s *Services) updateSensorData(g *gin.Context) {
	var json RawSensors
	isBound := g.ShouldBindJSON(&json)

	if isBound != nil {
		log.Println("[WARN] Received invalid json for /sendData", isBound.Error())
		g.JSON(http.StatusBadRequest, gin.H{"RECEIVED INVALID REQUEST": isBound.Error()})
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
		id := SensorId{id: currentSensor.Id}
		measurement := currentSensor.Measurment
		unit := currentSensor.Unit
		name := currentSensor.SensorName

		sensorData := SensorData{
			measurement: measurement,
			name:        name,
			unit:        unit,
			id:          id,
		}
		currentStatus := s.sensors.Update(sensorData)
		log.Println("[INFO] Received request to update sensor with the following", sensorData)

		// TODO don't fail right away, update sensors that are valid and
		// then return states for each sensor updated
		if currentStatus == false {
			g.JSON(http.StatusBadRequest, gin.H{"Update Sensor Data": currentStatus})
			return
		}
	}
	g.JSON(http.StatusOK, gin.H{"Update Sensor Data": true})
}

func (s *Services) getAvailableSensors(g *gin.Context) {
}

func (s *Services) getSensorData(g *gin.Context) {
	sensorId := g.Query("sensorId")
	data, err := s.sensors.GetSensorData(SensorId{id: sensorId})
	if err != nil {
		g.JSON(http.StatusBadRequest, gin.H{"Could not find sensor": sensorId})
		return
	}
	fmt.Println("Getting sensor Data", sensorId)
	serializedData := RawSensorData{
		SensorName: data.name,
		Id:         data.id.id,
		Status:     "",
		Unit:       data.unit,
		Measurment: data.measurement,
	}

	fmt.Println("Got", serializedData)
	g.JSON(http.StatusOK, serializedData)
	return
}

func main() {
	gin.SetMode(gin.ReleaseMode)
	r := gin.New()
	r.Use(cors.New(cors.Config{
		AllowOrigins: []string{"*"},
		AllowMethods: []string{"POST", "GET"},
		AllowHeaders: []string{"*"},
		//ExposeHeaders:    []string{"Content-Length"},
		AllowCredentials: false,
	}))

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
