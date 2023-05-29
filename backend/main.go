package main 

import (
	"net/http"
	"github.com/gin-gonic/gin"
)

type Sensor struct {
    measurement float32;
    name string;
    unit string;
}

type Services struct {
    authUrl string;
    SensorData map[string]Sensor;
}

type Response struct {
    StatusCode int;
    Headers map[string]string;
    Body string;
}


func (s* Services) postSensorData(g *gin.Context) {
    var json Sensor ;
    isValid := g.ShouldBindJSON(&json);
    if isValid != nil {
        g.JSON(http.StatusBadRequest, gin.H{"Invalid request for settting status": isValid.Error()});
        return
    }
    s.SensorData[json.name] = json;
    g.JSON(http.StatusOK, gin.H{"Recieved SensorData" : json.name});
}

func (s* Services) getAvailSensors(g* gin.Context) {
}

func (s* Services) waterSensorData(g* gin.Context) {
    // NOTE don't forget the auth!
}

func main() {
    router := gin.Default();
    services := new(Services);

    router.POST("/sendData", services.postSensorData);
    router.POST("/getAvailSenors", services.getAvailSensors);
    router.GET("/waterGarden", services.waterSensorData);

    router.Run(":8080");
}

