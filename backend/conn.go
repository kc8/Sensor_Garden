package main

import (
	"bufio"
	"fmt"
	"net"
	"net/http"
)

// locations of data in frame
const ( 
    // first part 
    fin = 1 << 7;
    rsv1 = 1 << 6;
    rsv2 = 1 << 5;
    rsv3 = 1 << 4;

    // second part
    mask =  1 << 7;
)

type MessageType int32;

// Frame or message types sec 11.8 and 5.2 as opcode
const ( 
    TextMessage MessageType = 1;
    BinaryMessage MessageType = 2;
    CloseFrame MessageType = 8;
    PingFrame  MessageType = 9; 
    PongFrame MessageType  = 10;
)

const (
    tlsScheme = "wss";
    scheme = "ws";
)

type WSConn struct {
    conn net.Conn; 
    DataType MessageType; 

    writeBuffer []byte
    readBuffer []byte
    //This buffer should be the same one we get back after the hijack call
    readWriteBuf bufio.ReadWriter
    clientAddr string

    Error func(
            w http.ResponseWriter, 
            r *http.Request, 
            status int, 
            reason error);  
    Upgrade func(writer http.ResponseWriter, request *http.Request);
    Protocol string;
}

type WriteError struct {
    Err error;
}

// Creates a conenction between client and server
// Default type of data to be transmitted is Text/UTF-8
// To change this type use SetMessageType(MessageType) 
func CreateConnection(conn net.Conn, readWriteBuffer bufio.ReadWriter, writeBuffer []byte) (*WSConn) {
    var newWSConn = &WSConn{
        conn: conn, 
        readWriteBuf: readWriteBuffer,
        writeBuffer: writeBuffer,
    }; 
    newWSConn.SetMessageType(TextMessage);
    return newWSConn; 
}

func (wsConn *WSConn) SetMessageType(dataType MessageType) { 
    wsConn.DataType = dataType;
}

func (wsConn *WSConn) Write(data []byte) WriteError { 

    var b0 byte = byte(wsConn.DataType) | fin; 
    var b1 byte = byte(len(data));
    // TODO look into masking if needed, although this is server code and most likely not needed
   
    var rawBuffer []byte = make([]byte, 0, 256);
    rawBuffer = append(rawBuffer, b0, b1);
    rawBuffer = append(rawBuffer, data...);

    var err error = nil;
    _, err =  wsConn.conn.Write(rawBuffer);
    // _, err =  wsConn.readWriteBuf.Write(rawBuffer);
    if (err != nil) { 
        return WriteError{Err: err};
    }
    return WriteError{};
}

// TODO and IDEAS we need to Reader.buffered to clear before we complete the ws connection 
// as there are things sitting in the buffer
// 1. I think we need to mimic what we do for the inital header in websocket.go to read? 
// from conn but I also thing we need to do something with the readWriteBuf?
func (wsConn *WSConn) Read() {
    var rawBuffer []byte = make([]byte, 0, 256);
    wsConn.conn.Read(rawBuffer);
    if len(rawBuffer) >  0 {
        fmt.Println(rawBuffer);
    }
    wsConn.readWriteBuf.Flush();
}
