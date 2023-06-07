## Sensor Garden

Using some temperature sensors and resistance sensors we are able to measure different environmental factors in a garden. 

Using a Raspberry Pi with sensors we can monitor things like temperature, soil moisture and more. The data gets sent a real time database were its then updated on the website below.

Have a look here at some of the live data: https://sensorgarden.cooperkyle.com/

## Technology Used

- Rust's Yew and WASM (hosted statically inside of Kubernetes)
- Bulma for CSS framework
- Backend written with gin-gonic in go (hosted inside of  Kubernetes)

## rpi-drivers
These are the drivers for the sensors as well as a way to upload the data to the backend. 

## Future Ideas: 
- re-write the rpi-drivers (they are a bit old and hard to manage)
- Add ability to 'water' the garden. I have the hardware to do this, but not the code
