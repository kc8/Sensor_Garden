## Sensor Garden

Using some temperature sensors and resistance sensors we are able to measure different environmental factors in a garden. 

Using a Raspberry Pi with sensors we can monitor things like temperature, soil moisture and more. The data gets sent a real time database were its then updated on the website below.

Have a look here at some of the live data: https://sensorgarden.cooperkyle.com/

## Technology Used

- Python with the some custom built modules for reading sensor values, and some from AdaFruit
- Firebase: Firestore, and Hosting
- GraphQL with Flask and Graphene 
- Google App Engine (for hosting with GraphQL)
- Google PubSub (will be used later for websockets)
- Google Cloud Functions (old method of getting measurements)
- Rust's Yew and WASM
- Bulma for CSS framework

## Future Ideas: 
- Light Sensor for measuring the suns rays (waiting on parts to arrive in the mail!)
- Pictures of the plant growth that are automatically taken and stored in the database. Picture would be taken 1 - 3 times a day and updated? 
- A time series report of values
- Ability to automatically and manually water the garden when the soil needs it + monitoring (waiting on parts to arrive in the mail!)
- A better method of quantifying moisture levels 
- 
