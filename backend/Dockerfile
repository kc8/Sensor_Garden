FROM golang:1.20
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go build -v ./...
CMD ["/app/com.cooperkyle.sesnorgardenbackend"]
