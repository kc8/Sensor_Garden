import React, { Component } from 'react';
import gql from "graphql-tag"
import { ApolloClient } from "apollo-client";
import { InMemoryCache, DefaultOptions} from "apollo-cache-inmemory";
import { HttpLink } from "apollo-link-http";

const getSensorValues = gql`
    query {
        measurements {
        sensorName
        sensorMeasurement
        }
    }`;

const cache = new InMemoryCache();

const link = new HttpLink({
  uri: "https://tomato-sensor.ue.r.appspot.com/"
});

const defaultOptions  = {
    watchQuery: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'ignore',
    },
    query: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'all',
    },
  }

const client = new ApolloClient({
  link,
  cache,
  defaultOptions: defaultOptions
});


class SensorData extends Component {

    constructor(props) {
        super(props)
        this.state = {
            measurements: []
        }
    }

    componentDidMount() { 
        this.getData();
        setInterval(this.getData, 10000);
    }

    getData = () => {
        client.query({
            query: getSensorValues
        }).then(result => this.setState(result.data)
    )}

    render() {
        return (
            <div>
                <section className="hero">
                    <div className="hero-body">            
                        <div className="tile is-ancestor">
                        <div className="tile is-parent">
                            {
                                this.state.measurements.map(({sensorName, sensorMeasurement}) => (
                                    <article key={sensorName} className="tile is-child box"> 
                                        <p className="title">{sensorName}</p>
                                        <p className="subtitle">{sensorMeasurement}</p>
                                    </article> 
                                ))
                            }
                        </div>
                        </div>
                    </div>
                </section>
            </div>
                
        )
    }
}


export default SensorData;