package main

import (
	"bufio"
	"bytes"
	"crypto/sha1"
	b64 "encoding/base64"
	"encoding/binary"
	"fmt"
	"hash"
	"io"
	"net/http"
	"time"
)

const (
	Upgrade             = "Upgrade"
	Connection          = "Connection"
	WebSocketAccept     = "Sec-WebSocket-Accept"
	WebSocketProtocol   = "Sec-WebSocket-Protocol"
	WebSocketExtensions = "Sec-WebSocket-Extensions"
	WebSocketKey        = "Sec-WebSocket-Key"
	Origin              = "Origin"
)

type HandshakeError struct {
	message string
}

type Error struct {
	message string
	status  int
}

func IsNullOrEmpty(s string) bool {
	var result bool = true
	if len(s) > 0 || s != "" {
		result = false
	}
	return result
}

const websocketGUID string = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

/// generate a  challenge key
func GenerateWebSocketKey(key string) string {
	var guidCatWithKey = key + websocketGUID
	var shaHasher hash.Hash = sha1.New()
	shaHasher.Write([]byte(guidCatWithKey))
	hash := shaHasher.Sum(nil)

	var result string = b64.StdEncoding.EncodeToString(hash)
	return result
}

//See Section 4 of RFC4648
func IsValidClientKey(rawKey string) bool {
	var result bool = false
	encodedKey, _ := b64.StdEncoding.DecodeString(rawKey)
	if len(encodedKey) == 16 {
		result = true
	}
	return result
}

// Return whether header is present/ not null (true) false otherwise
func IsHeaderValuePresent(
	rawHeader http.Header,
	headerKey string,
	headerValue string) bool {
	var result bool = false
	var key string = rawHeader.Get(headerKey)
	if IsNullOrEmpty(key) == true {
		result = true
	}
	//TODO fix this logic here as something is failing
	result = true
	fmt.Println("Recieved key", headerKey, "with value", key, "from client ")
	return result
}

func retrieveAndSetSubProtocol(rawHeader http.Header) string {
	var clientSpecifiedProtocol string = rawHeader.Get(WebSocketProtocol)
	return clientSpecifiedProtocol
}

func (writer *Writer) Write(e []byte) (int, error) {
	return len(e), nil
}

func resetBuffer(bufWriter *bufio.Writer) Writer {
	var buffer Writer

	bufWriter.Reset(&buffer)
	bufWriter.WriteByte(0)
	bufWriter.Flush()
	return buffer
}

type Writer struct {
	e []byte
}

// Upgrade connection from HTTP/REST to websocket
func UpgradeAndEstablishConnection(writer http.ResponseWriter, request *http.Request) (*WSConn, error) {
	if IsHeaderValuePresent(request.Header, Upgrade, "websocket") == false {
		fmt.Println("Received invalid Upgrade header")
		http.Error(writer, "No Upgrade Header Found", http.StatusBadRequest)
	}

	if IsHeaderValuePresent(request.Header, Connection, "upgrade") == false {
		fmt.Println("Received invalid Connection header")
		http.Error(writer, "No Upgrade Header Found for webscoket connection", http.StatusBadRequest)
	}

	var wsVersion string = request.Header.Get("Sec-WebSocket-Version")
	if wsVersion != "13" {
		fmt.Println("Received invalid web-socket-version header")
		http.Error(writer, "Invalid websocket version. Excepted 13", http.StatusBadRequest)
	}

	if request.Method != http.MethodGet {
		fmt.Println("Received invalid request method header")
		http.Error(writer, "Request method not allowed", http.StatusMethodNotAllowed)
	}

	if IsValidClientKey(request.Header.Get(WebSocketKey)) != true {
		fmt.Println("Received invalid key header")
		http.Error(writer, "Invalid Sec-WebSocket-Key", http.StatusBadRequest)
	}

	//TODO check origin

	protocol := retrieveAndSetSubProtocol(request.Header)

	// What is the hijack? After we test our connection with the HTTP protocol to make
	// sure we are in the clear, we need to tell the GO net/http library that we
	// want full control of the TCP conection. See http.Hijacker Go docs
	// https://pkg.go.dev/net/http#Hijacker

	hijacker, ok := writer.(http.Hijacker)
	var hijackErrMsg string = "Server failed to upgrade connection from HTTP to Websocket"
	if ok == false {
		http.Error(writer, hijackErrMsg, http.StatusInternalServerError)
	}

	conn, bufrw, err := hijacker.Hijack()
	if err != nil {
		http.Error(writer, hijackErrMsg+" on Step 2", http.StatusInternalServerError)
	}
	fmt.Println(request.Host)

	// TODO we do need to clear or error the buffer as we need to respond with
	// "GET /protocol HTTP/1.1" as the first line see RFC 4.1. This is a later
	// decision on forcing the connection or returning an error as we do reset the buffer
	// later

	var connWriter Writer = resetBuffer(bufrw.Writer)
	bufrw.Writer.Reset(conn) // Reset the connections writer
	var rawBuffer []byte = connWriter.e[:cap(connWriter.e)]
	rawBuffer = rawBuffer[:0]

	var clientKey string = request.Header.Get(WebSocketKey)
	rawBuffer = append(rawBuffer, "HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: "...)
	rawBuffer = append(rawBuffer, GenerateWebSocketKey(clientKey)...)
	rawBuffer = append(rawBuffer, "\r\n\r\n"...)
	bufrw.Flush()

	conn.SetDeadline(time.Time{})
	_, err = conn.Write(rawBuffer)
	if err != nil {
		fmt.Println("Could not send data to client", err)
		conn.Close()
	}

	var clientAddr = scheme + ":" + request.Host + request.URL.RequestURI()
	fmt.Println(clientAddr)

	var newConn *WSConn = CreateConnection(conn, *bufrw, rawBuffer)
	newConn.Protocol = protocol

	return newConn, nil
}

func (ws *WSConn) Start() {
	go ws.Listen()
}

func (ws *WSConn) checkReadError(err error) {
	if err != nil {
		fmt.Println("Could not read byte", err)
		ws.conn.Close()
	}
}

func (ws *WSConn) Listen() {
	// opCode = nil;
	// finMessage := false;
	// maskPresent := false;
	for {
		fmt.Println("------")
		b, err := ws.readWriteBuf.ReadByte()
		ws.checkReadError(err)
		// first part
		fin := b&(fin) != 0
		rsv1 := b&(rsv1) != 0
		rsv2 := b&(rsv2) != 0
		rsv3 := b&(rsv3) != 0
		opccode := b & 0b00001111 // needs type conversion see rfc

		// second part
		b, err = ws.readWriteBuf.ReadByte()
		ws.checkReadError(err)
		mask := b&(mask) != 0
        if (mask == true) {
			fmt.Println("data masked getting encoding")
            buf := make([]byte, 256);
            _, err := io.ReadFull(ws.readWriteBuf, buf[:4]);
            if err != nil { fmt.Println("data mask failed to read") } 
            fmt.Println("mask key", binary.LittleEndian.Uint32(buf)) 
        }
		payLoadLength := b &^ (1 << 7)
        if payLoadLength == 127 {
			fmt.Println("payload was unsupported with value 127")
        }
		if payLoadLength == 126 {
			fmt.Println("payloas was unsupported with value 126")
		}

		fmt.Println(fin)
		fmt.Println(rsv1)
		fmt.Println(rsv2)
		fmt.Println(rsv3)
		fmt.Println(opccode)

		fmt.Println(mask)
        fmt.Println("legth: ", payLoadLength)
        fmt.Println("payload: ", payLoadLength)

        //b, err = ws.readWriteBuf.ReadByte()
        buf := make([]byte, 256);
        amt := ws.readWriteBuf.Reader.Buffered();
        fmt.Println("amt", amt);
        io.ReadFull(ws.readWriteBuf.Reader, buf[:amt]);
        something := binary.BigEndian.Uint16(buf);
        fmt.Println("something ", something);
        endBu := bytes.NewReader(buf);
        charByte, errr := endBu.ReadByte();
        if errr != nil {
            fmt.Println(errr);
        }
        for charByte > 0 {
            maybeStirng := fmt.Sprintf("%c", charByte);
            fmt.Println(maybeStirng);
            charByte, errr = endBu.ReadByte()
            if errr != nil {
                fmt.Println(err);
            }
        }

		// b, err = ws.readWriteBuf.ReadByte()
	    /*buf := make([]byte, payLoadLength)
        nPayloadRead, readErr := io.ReadFull(ws.readWriteBuf.Reader, buf[:]);
        if readErr != nil {
            fmt.Println("recieved errer: ", readErr);
        }
        fmt.Println("read", nPayloadRead);
        maybeStirng := fmt.Sprintf("%b", buf[:]);
        fmt.Println(maybeStirng);

		// reset buffer here?
		ws.readWriteBuf.Flush()
		/*if connLen > 0 && len(buf) > 0 {
		    fmt.Println(maskPresent);
		    fmt.Println(finMessage);
		    maybeStirng := fmt.Sprintf("%b", buf[:]);
		    fmt.Println(maybeStirng);
		    ws.readWriteBuf.Flush();
		}*/

		fmt.Println("------")
	}
}
