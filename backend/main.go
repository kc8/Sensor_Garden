package main

import (
	"fmt"
	"log"
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

func (s* Services) getAvailSensors(g* gin.Context) {
}

func (s* Services) waterSensorData(g* gin.Context) {
    // NOTE don't forget the auth!
}

func main() {
    http.HandleFunc("/sendData", startCommsForData);
    log.Fatal(http.ListenAndServe(":8080", nil));
}

func startCommsForData(w http.ResponseWriter, r *http.Request) {
	fmt.Println("received WS upgrade connection request from client");
	ws, err := UpgradeAndEstablishConnection(w, r);
	if err != nil { 
        log.Fatal("Recieved invalid website when upgrading connection");
	}
    ws.Start();
}

func sendTestMessage(conn *WSConn) {
	var rawBuffer []byte;
	conn.SetMessageType(TextMessage);
    rawBuffer = rawBuffer[:0];
    rawBuffer = append(rawBuffer, "TEST"...);
	var err WriteError = conn.Write(rawBuffer);
    if err.Err != nil { 
        fmt.Println("Failed to send TEST data to client", err.Err);
    }
}
