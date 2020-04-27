import React, {Fragment, useState, useEffect, Component } from 'react';
import {useQuery} from "@apollo/react-hooks"; 
import gql from "graphql-tag"
import { Query } from '@apollo/react-components';
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

const defaultOptions: DefaultOptions = {
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
        }).then(result => this.setState(result.data)//result.data.measurements
        //         .map(({sensorName, sensorMeasurement}) => (
        //             this.setState({[sensorName]: sensorMeasurement})
        //             //console.log(sensorName, sensorMeasurement)
        //             ))
                )
    }
    //this.setState({[sensorName]:sensorMeasurement})
    renderData() {
        return this.state.sensorMeasurements.map(({sensorName, sensorMeasurement}) => (
            <div key={sensorName}> 
                <p> 
                    {sensorName} : {sensorMeasurement}
                </p>
            </div>
        ))
    }
    
    render() {
        return (
                <div>
                     {
                        this.state.measurements.map(({sensorName, sensorMeasurement}) => (
                            <div key={sensorName}> 
                                <p> 
                                    {sensorName} : {sensorMeasurement}
                                </p>
                            </div> 
                        ))
                     }
                </div>   
        )
    }
}


export default SensorData;